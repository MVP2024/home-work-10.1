import json
from typing import Any, Dict, List

from src.logger import setup_logger

# Настройка логгера для модуля utils
logger = setup_logger("utils")

# Логируем инициализацию модуля
logger.info("Инициализация модуля utils")


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о транзакциях из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях или пустой список.
    """
    logger.debug(f"Попытка загрузить транзакции из файла: {file_path}")  # Логируем попытку загрузки
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций.")  # Логируем успешную загрузку

                return data
            logger.warning("Загруженные данные не являются списком. Возвращается пустой список.")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")  # Логируем ошибку
        return []
    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Ошибка при загрузке JSON: {e}")  # Логируем ошибку
        return []
