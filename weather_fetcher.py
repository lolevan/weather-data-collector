import time
import requests
from datetime import datetime
from database import Session
from models import WeatherData
from utils import degrees_to_cardinal, hpa_to_mmhg, weather_code_to_precipitation_type


def fetch_weather_data(interval):
    """
    Функция для периодического запроса данных погоды и сохранения их в базу данных.
    :param interval: Интервал времени между запросами в секундах
    """
    session = Session()
    while True:
        try:
            # Параметры запроса (координаты Сколтеха)
            params = {
                'latitude': 55.7539,
                'longitude': 37.6208,
                'hourly': 'pressure_msl,precipitation,weather_code',
                'current_weather': True,
                'windspeed_unit': 'ms',
                'precipitation_unit': 'mm',
                'timezone': 'Europe/Moscow',
                'past_hours': 1,  # Добавим прошедший час для получения ближайших данных
                'forecast_hours': 1  # И следующий час для получения ближайших данных
            }
            response = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
            data = response.json()

            current = data['current_weather']
            temperature = current.get('temperature')
            wind_speed = current.get('windspeed')
            wind_direction_deg = current.get('winddirection')
            wind_direction = degrees_to_cardinal(wind_direction_deg)

            # Получаем текущее время и преобразуем в объект datetime
            current_time_str = current.get('time')
            current_time = datetime.strptime(current_time_str, '%Y-%m-%dT%H:%M')

            # Получаем список времен из hourly данных и преобразуем в объекты datetime
            hourly_times_str = data['hourly']['time']
            hourly_times = [datetime.strptime(t, '%Y-%m-%dT%H:%M') for t in hourly_times_str]

            # Находим индекс ближайшего времени
            time_differences = [abs((t - current_time).total_seconds()) for t in hourly_times]
            index = time_differences.index(min(time_differences))

            # Получаем давление и осадки из hourly данных
            pressure_hpa = data['hourly']['pressure_msl'][index]
            pressure_mmhg = hpa_to_mmhg(pressure_hpa)
            precipitation_amount = data['hourly']['precipitation'][index]
            weather_code = data['hourly']['weather_code'][index]
            precipitation_type = weather_code_to_precipitation_type(weather_code)

            # Создаем запись в базе данных
            weather_entry = WeatherData(
                temperature=temperature,
                wind_speed=wind_speed,
                wind_direction=wind_direction,
                pressure=pressure_mmhg,
                precipitation_type=precipitation_type,
                precipitation_amount=precipitation_amount
            )
            session.add(weather_entry)
            session.commit()
            print(f"[{datetime.now()}] Данные погоды добавлены в базу данных.")

        except Exception as e:
            print(f"Ошибка при получении данных: {e}")

        # Ждем указанный интервал времени
        time.sleep(interval)
