import re
from collections import Counter
from typing import Any, Dict, List


def filter_bank_operations(transactions: List[Dict[str, Any]], search_str: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских операций по заданной строке поиска.
    Параметры:
    transactions : List[Dict[str, Any]]
        Список транзакций, где каждая транзакция представлена в виде словаря.
    Search_str : str
        Строка поиска, по которой будет производиться фильтрация.
    Возвращает:
    List[Dict[str, Any]]
        Список транзакций, которые содержат строку поиска в описании.

    Исключения:
    ValueError
        Если transactions не является списком или search_str не является строкой.
    """

    if not isinstance(transactions, list):
        raise ValueError("transactions должен быть списком словарей")
    if not isinstance(search_str, str):
        raise ValueError("search_str должен быть строкой")

    if not search_str.strip():
        return []  # Возвращаем пустой список, если строка поиска пустая

    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    filtered_transactions = []

    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        # Проверяем, содержит ли транзакция описание, соответствующее строке поиска
        if (
            "description" in transaction
            and isinstance(transaction["description"], str)
            and pattern.search(transaction["description"])
        ):
            filtered_transactions.append(transaction)

    return filtered_transactions


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям на основе описания транзакций.

    Параметры:
    transactions (List[Dict[str, Any]]): Список транзакций, где каждая транзакция представлена как словарь.
    categories (List[str]): Список категорий, по которым нужно подсчитать количество транзакций.

    Возвращает:
    Dict[str, int]: Словарь, где ключами являются категории, а значениями — количество транзакций для каждой категории.

    Исключения:
    ValueError: Если хотя бы одна транзакция не является словарем.
    """

    # Проверка, что каждая транзакция является словарем
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise ValueError("Каждый элемент transactions должен быть словарем.")

    category_count = {category: 0 for category in categories}

    descriptions = [transaction.get("description", "").lower() for transaction in transactions]

    category_counter: Counter[str] = Counter()  # Аннотация типа для category_counter

    for description in descriptions:
        for category in categories:
            category_lower = category.lower()
            if category_lower in description:
                category_counter[category] += 1
                break

    for category in category_count:
        category_count[category] += category_counter[category]

    return category_count
