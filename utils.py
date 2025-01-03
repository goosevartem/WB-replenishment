import io
import pandas as pd

def calculate_replenishment(average_monthly_sales, current_stock, min_stock, delivery_time_weeks, in_transit_stock):
    """
    Рассчитывает количество товара для допоставки с учетом минимального запаса, срока доставки,
    продаж за период и товаров в пути.

    :param average_monthly_sales: Среднемесячные продажи
    :param current_stock: Текущий остаток на складе
    :param min_stock: Минимальный остаток на складе
    :param delivery_time_weeks: Срок поставки в неделях
    :param in_transit_stock: Товары в пути
    :return: Количество товара для допоставки
    """
    # Установка значений по умолчанию для отсутствующих данных
    average_monthly_sales = max(0, average_monthly_sales or 0)
    current_stock = max(0, current_stock or 0)
    min_stock = max(0, min_stock or 0)
    delivery_time_weeks = max(1, delivery_time_weeks or 1)
    in_transit_stock = max(0, in_transit_stock or 0)

    # Рассчитываем продажи за период доставки
    sales_during_delivery = (average_monthly_sales / 4) * delivery_time_weeks

    # Прогнозируемый остаток после периода доставки, включая товары в пути
    projected_stock = max(0, current_stock + in_transit_stock - sales_during_delivery)

    # Рассчитываем требуемый запас
    required_stock = min_stock + sales_during_delivery

    # Рассчитываем допоставку
    replenishment = max(0, required_stock - projected_stock)

    return replenishment







def download_excel(dataframe, filename='result.xlsx'):
    try:
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            dataframe.to_excel(writer, index=False, sheet_name='Результаты')
        output.seek(0)
        return output
    except Exception as e:
        st.error(f"Ошибка при создании Excel-файла: {e}")
        return None

