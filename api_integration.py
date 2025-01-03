import requests
import pandas as pd
import streamlit as st  # Добавлено для работы с Streamlit

# Конфигурация
API_URL = "https://statistics-api.wildberries.ru"
TOKEN = "ВВЕДИ ТОКЕН"  # Убедитесь, что здесь указан актуальный токен

def fetch_sales(date_from):
    """Получение данных о продажах за указанный период."""
    url = f"{API_URL}/api/v1/supplier/sales"
    headers = {
        "Authorization": TOKEN  # Убедитесь, что токен указан корректно
    }
    params = {
        "dateFrom": date_from  # Формат даты: YYYY-MM-DD или YYYY-MM-DDTHH:MM:SS
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Вызывает ошибку, если статус не 200
        return response.json()
    except requests.exceptions.HTTPError as e:
        st.error(f"Ошибка при запросе данных о продажах: {e}")
        raise
    except Exception as e:
        st.error(f"Неизвестная ошибка при запросе данных о продажах: {e}")
        raise

def fetch_stocks(date_from):
    """Получение данных об остатках."""
    url = f"{API_URL}/api/v1/supplier/stocks"
    headers = {"Authorization": TOKEN}
    params = {"dateFrom": date_from}  # Добавляем параметр dateFrom

    try:
        response = requests.get(url, headers=headers, params=params)
        response.encoding = 'utf-8'  # Устанавливаем правильную кодировку
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка при запросе данных об остатках: {e}")
        raise

def parse_sales(data):
    """Парсинг данных о продажах в DataFrame."""
    try:
        df = pd.DataFrame(data)
        if 'nmId' not in df.columns:
            raise ValueError("Отсутствует столбец 'nmId' в данных о продажах")
        return df
    except ValueError as e:
        st.error(f"Ошибка при обработке данных о продажах: {e}")
        return pd.DataFrame()

def parse_stocks(data):
    """Парсинг данных об остатках в DataFrame."""
    try:
        df = pd.DataFrame(data)
        if 'nmId' not in df.columns:
            raise ValueError("Отсутствует столбец 'nmId' в данных об остатках")
        return df
    except ValueError as e:
        st.error(f"Ошибка при обработке данных об остатках: {e}")
        return pd.DataFrame()

