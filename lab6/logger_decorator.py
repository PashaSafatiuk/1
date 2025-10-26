# logger_decorator.py
from datetime import datetime


def logger(level="INFO"):
    """
    Декоратор для логування повідомлень у консоль
    рівнів: info, warning, error
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            colors = {
                "INFO": "\033[92m",  # зелений
                "WARNING": "\033[93m",  # жовтий
                "ERROR": "\033[91m",  # червоний
                "RESET": "\033[0m"
            }

            color = colors.get(level.upper(), colors["RESET"])
            print(f"{color}[{level.upper()}] {time} → Виконується {func.__name__}{colors['RESET']}")

            try:
                result = func(*args, **kwargs)
                print(f"{color}[{level.upper()}] {time} → Успішно виконано{colors['RESET']}")
                return result
            except Exception as e:
                print(f"{colors['ERROR']}[ERROR] {time} → Помилка: {e}{colors['RESET']}")
                raise e

        return wrapper

    return decorator
