# Weather Data Collector

Weather Data Collector — это Python-приложение, которое автоматически собирает данные о погоде в районе Сколтеха через заданные промежутки времени и сохраняет их в базу данных. Также приложение позволяет экспортировать последние 10 записей в файл Excel (.xlsx) по команде из консоли.

## Особенности

- **Автоматический сбор данных о погоде** с использованием API Open-Meteo.
- **Пользовательский ввод интервала времени** между запросами данных.
- **Сохранение данных в базу данных** SQLite с использованием ORM SQLAlchemy.
- **Экспорт данных в Excel**: по команде из консоли последние 10 записей экспортируются в файл `weather_data.xlsx`.
- **Асинхронная работа функций** сбора данных и обработки команд пользователя с использованием модуля `threading`.
- **Чистый и хорошо структурированный код**, соответствующий стандартам PEP8 и снабженный комментариями.

## Требования

- Python 3.6 или выше
- Установленные зависимости из файла `requirements.txt`

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/lolevan/weather-data-collector.git
   cd weather-data-collector
   ```

2. **Создайте и активируйте виртуальное окружение (рекомендуется):**

   ```bash
   python -m venv venv
   # Для Windows:
   venv\Scripts\activate
   # Для Unix или MacOS:
   source venv/bin/activate
   ```

3. **Установите необходимые зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

## Использование

1. **Запустите приложение:**

   ```bash
   python main.py
   ```

2. **При запуске приложение запросит у вас интервал времени между запросами данных (в секундах):**

   ```
   Введите интервал времени между запросами данных (в секундах):
   ```

   Введите желаемый интервал, например, `180` для сбора данных каждые 3 минуты.

3. **Приложение начнет собирать данные о погоде в фоновом режиме.**

4. **Вы можете вводить команды в консоли:**

   - `export` — экспортирует последние 10 записей из базы данных в файл `weather_data.xlsx` в папке проекта.
   - `exit` — завершает работу программы.
