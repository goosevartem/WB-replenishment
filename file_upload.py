# Файл: file_upload.py
import streamlit as st
import pandas as pd
from api_integration import fetch_sales, fetch_stocks, parse_sales, parse_stocks

def handle_file_upload():
    """Обработка загрузки данных через файл или API."""
    data_source = st.radio(
        "Выберите источник данных:",
        ("Загрузка файла", "Загрузка через API"),
        key="data_source_radio_key"  # Уникальный ключ
    )

    if data_source == "Загрузка файла":
        uploaded_file = st.file_uploader("Загрузите файл с данными (формат: CSV или Excel)", type=["csv", "xlsx"], key="file_uploader_key")
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)
            data.fillna(0, inplace=True)
            st.success("Файл успешно загружен!")
            return data
        else:
            st.warning("Пожалуйста, загрузите файл.")
            return None
    elif data_source == "Загрузка через API":
        with st.spinner("Загружаем данные через API..."):
            try:
                sales_data = fetch_sales("2024-01-01")
                stocks_data = fetch_stocks("2019-06-20")

                # Преобразование данных
                df_sales = parse_sales(sales_data)
                df_stocks = parse_stocks(stocks_data)

                # Проверка наличия данных
                if df_sales.empty or df_stocks.empty:
                    st.error("Данные не найдены или пусты.")
                    return None

                # Объединение данных в один DataFrame
                data = pd.merge(df_sales, df_stocks, on="nmId", how="outer")
                st.success("Данные успешно загружены через API!")
                return data
            except Exception as e:
                st.error(f"Ошибка загрузки данных через API: {e}")
                st.write("Данные о продажах после преобразования:", df_sales.head())
                st.write("Данные об остатках после преобразования:", df_stocks.head())
                st.write("Объединенные данные:", data.head())
                return None
