# Файл: main.py
import streamlit as st
import pandas as pd
from utils import calculate_replenishment, download_excel
from file_upload import handle_file_upload

# Заголовок приложения
st.title('Расчет допоставки товаров для Wildberries')

# Описание
st.write("""
    Это приложение помогает рассчитать, сколько товара нужно заказать для допоставки на маркетплейс Wildberries,
    исходя из прогнозируемых продаж, текущих остатков, минимальных остатков, товаров в пути и сроков доставки.
""")

# Загрузка таблицы с данными
df_result = handle_file_upload()

# Вывод результатов и возможность скачивания
if df_result is not None:
    # Проверка размера данных
    st.write(f"Размер DataFrame: {df_result.shape[0]} строк, {df_result.shape[1]} столбцов")

    # Отображение первых 100 строк
    if df_result.shape[0] > 100:
        st.warning("Показываются только первые 100 строк.")
        st.dataframe(df_result.head(100))
    else:
        st.dataframe(df_result)

    # Возможность скачивания всех данных
    st.write("Скачать полный результат:")
    excel_file = download_excel(df_result)
    st.download_button(
        label="Скачать Excel",
        data=excel_file,
        file_name='result.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


    # Скачивание результатов
    st.write("Скачать результат в формате Excel:")
    excel_file = download_excel(df_result)
    st.download_button(
        label="Скачать Excel",
        data=excel_file,
        file_name='result.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    st.write("Скачать результат в формате CSV:")
    csv_data = df_result.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="Скачать CSV",
        data=csv_data,
        file_name='result.csv',
        mime='text/csv'
    )
