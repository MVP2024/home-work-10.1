from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций.

    Аргументы:
        filename: Имя файла для записи логов. Если None, выводит в консоль.
    """

    def write_log(information: str) -> None:
        """Записывает информацию в файл или выводит в консоль."""
        if filename:
            with open(filename, "a") as f:
                f.write(information + "\n")
        else:
            print(information)
