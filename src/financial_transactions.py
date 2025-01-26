import csv
import os
from typing import Dict, List, Any, Hashable

import pandas as pd


class EmptyFileError(Exception):
    """Исключение для случая, когда файл пуст."""

    pass


class FileReadError(Exception):
    """Исключение для случая, когда файл не может быть прочитан."""

    pass


class InvalidFileFormatError(Exception):
    """Исключение для случая, когда файл не является форматом Excel."""

    pass


def read_financial_operations_from_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из файла csv
    :param file_path: Путь к файлу
    :return: Список словарей с транзакциями.
    :raises FileReadError: Если файл не может быть прочитан.
    :raises EmptyFileError: Если файл пуст или не содержит данных.
    :raises InvalidFileFormatError: Если файл не является форматом CSV.
    :raises FileNotFoundError: Если файл не существует.
    """
    # Проверка на существование файла
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    # Проверка на расширение файла
    if not file_path.endswith(".csv"):
        raise InvalidFileFormatError("Файл должен быть в формате .csv")

    transactions_from_csv: List[Dict[str, str]] = []  # Изменено на List[Dict[str, str]]
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions_from_csv.append(row)
    except Exception as e:
        raise FileReadError(f"Не удалось прочитать файл: {e}")

    if not transactions_from_csv:
        raise EmptyFileError("Файл пуст или не содержит данных.")

    return transactions_from_csv


from typing import List, Dict, Any

def read_financial_operations_from_excel(file_path: str) -> list[dict[Hashable, Any]]:
    """
    Считывает финансовые операции из файла xlsx
    :param file_path: Путь к файлу
    :return: Список словарей с транзакциями.
    :raises FileReadError: Если файл не может быть прочитан.
    :raises EmptyFileError: Если файл пуст или не содержит данных.
    :raises InvalidFileFormatError: Если файл не является форматом Excel.
    :raises FileNotFoundError: Если файл не существует.
    """
    # Проверка на существование файла
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    # Проверка на расширение файла
    if not file_path.endswith(".xlsx"):
        raise InvalidFileFormatError("Файл должен быть в формате .xlsx")

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise FileReadError(f"Не удалось прочитать файл: {e}")

    transactions_from_xlsx = df.to_dict(orient="records")

    if not transactions_from_xlsx:
        raise EmptyFileError("Файл пуст или не содержит данных.")

    return transactions_from_xlsx
