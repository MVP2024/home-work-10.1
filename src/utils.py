import json
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о транзакциях из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях или пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Ошибка при загрузке JSON: {e}")  # Сообщение для проверки.
        return []
