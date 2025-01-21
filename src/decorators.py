from datetime import datetime
from functools import wraps
from time import sleep
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None, time_delay: float = 0) -> Callable:
    """Декоратор для логирования вызовов функций с задержкой

    Аргументы:
    filename: Имя файла для записи логов. Если (Нет)None, выводит в консоль.
    time_delay: задержка времени по-умолчанию = 0
    """

    def write_log(information: str) -> None:
        """Записывает информацию в файл или выводит в консоль."""
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(information + "\n")
        else:
            print(information)

    def decorator(function: Callable) -> Callable:
        """Декоратор для функции, который добавляет запись в log."""

        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обёртка функции для логирования вызовов и обработки ошибок"""
            sleep(time_delay)  # Добавляем временную задержку
            start_time = datetime.now()
            write_log(f"Начало {function.__name__} в {start_time.isoformat()}  с аргументами: {args}, {kwargs}")
            try:
                result = function(*args, **kwargs)  # Выполняем функцию и сохраняем результат.
                end_time = datetime.now()
                execution_time = end_time - start_time  # расчёт время выполнения функции
                # Запись об успешном завершении.
                write_log(
                    f"{function.__name__} ok. " f"Возвращаемое значение {result}. Время выполнения: {execution_time}",
                )
                return result  # Возвращаем резкльтат функции
            except Exception as e:
                write_log(
                    f"{function.__name__}) error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}. Ошибка: {str(e)}",
                )
                raise  # Повторно выводим исключение

        return wrapper

    return decorator
