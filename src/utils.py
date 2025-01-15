import json
import os
from typing import List, Dict

def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает финансовые транзакции из JSON-файла.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        # Проверяем, пустой ли файл
        if os.path.getsize(file_path) == 0:
            return []

        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

        # Проверяем, является ли загруженные данные списком
        if isinstance(data, list):
            return data
        else:
            return []
