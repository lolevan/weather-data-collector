import threading
from weather_fetcher import fetch_weather_data
from exporter import export_to_excel


def main():
    # Запрашиваем у пользователя интервал времени в секундах
    while True:
        try:
            interval = int(input("Введите интервал времени между запросами данных (в секундах): "))
            if interval <= 0:
                print("Пожалуйста, введите положительное число.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    # Запускаем поток для сбора данных о погоде с указанным интервалом
    data_thread = threading.Thread(target=fetch_weather_data, args=(interval,))
    data_thread.daemon = True
    data_thread.start()

    # Основной цикл программы для обработки команд пользователя
    while True:
        command = input("Введите команду (export для экспорта данных, exit для выхода): ")
        if command.lower() == 'export':
            export_to_excel()
        elif command.lower() == 'exit':
            print("Завершение работы программы.")
            break
        else:
            print("Неизвестная команда.")


if __name__ == '__main__':
    main()
