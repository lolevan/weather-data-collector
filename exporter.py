import pandas as pd
from database import Session
from models import WeatherData


def export_to_excel():
    """
    Функция для экспорта последних 10 записей из базы данных в файл Excel.
    """
    session = Session()
    # Получаем последние 10 записей
    entries = session.query(WeatherData).order_by(WeatherData.id.desc()).limit(10)
    # Преобразуем в DataFrame
    df = pd.DataFrame([{
        'Время': entry.timestamp,
        'Температура (°C)': entry.temperature,
        'Скорость ветра (м/с)': entry.wind_speed,
        'Направление ветра': entry.wind_direction,
        'Давление (мм рт. ст.)': entry.pressure,
        'Тип осадков': entry.precipitation_type,
        'Количество осадков (мм)': entry.precipitation_amount
    } for entry in entries])
    # Экспортируем в Excel
    df.to_excel('weather_data.xlsx', index=False)
    print("Данные успешно экспортированы в файл weather_data.xlsx")
