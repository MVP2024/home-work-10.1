import re
from collections import Counter, defaultdict
from typing import List, Dict, Union, Any


def filter_bank_operations(transactions: List[Dict[str, Any]], search_str: str) -> List[Dict[str, Any]]:
    """
    Фильтрует банковские операции по строке поиска в любом поле.

    :param transactions: Список словарей, представляющих банковские операции.
                        Ожидается, что каждый словарь может содержать различные ключи.
    :param search_str: Строка для поиска в любых полях каждой операции.
    :return: Список словарей, которые содержат данную строку в любом из своих значений.
    :raises ValueError: Если transactions не является списком или search_str не является строкой.
    """
    # Проверяем тип входных данных
    if not isinstance(transactions, list):
        raise ValueError("transactions должен быть списком словарей")
    if not isinstance(search_str, str):
        raise ValueError("search_str должен быть строкой")

    # Если строка поиска пустая
    if not search_str:
        print("Строка поиска не может быть пустой.")
        return []

    # Скомпилируем регулярное выражение для поиска
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)

    filtered_transactions = []

    # Фильтруем операции
    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue  # Пропускаем элементы, которые не являются словарями

        # Проверяем все значения в словаре
        for value in transaction.values():
            if isinstance(value, str) and pattern.search(value):
                filtered_transactions.append(transaction)
                break  # Выходим из цикла, если нашли совпадение

    # Если совпадений не найдено, выводим сообщение
    if not filtered_transactions:
        print(f"Нет операций, соответствующих критерию поиска '{search_str}'.")

    return filtered_transactions


from collections import Counter
from typing import List, Dict, Union


def count_transactions_by_category(transactions: List[Dict[str, Union[str, float]]],
                                   categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по категориям.
    """
    # Проверяем тип входных данных
    if not isinstance(transactions, list):
        raise ValueError("transactions должен быть списком словарей")
    if not isinstance(categories, list):
        raise ValueError("categories должен быть списком строк")

    # Инициализируем Counter для подсчета категорий
    category_count = Counter()
    missing_description_count = 0  # Счетчик пропущенных описаний

    # Обрабатываем каждую банковскую операцию
    for transaction in transactions:
        # Проверяем, является ли элемент словарем
        if not isinstance(transaction, dict):
            continue  # Игнорируем некорректные элементы

        # Получаем описание операции
        description = transaction.get('description')

        # Если описание отсутствует или пустое, увеличиваем счетчик
        if description is None or description == '':
            missing_description_count += 1
            continue

        # Подсчитываем количество вхождений для каждой категории
        category_count[description] += 1

    # Преобразуем Counter в обычный словарь и добавляем категории, которые не были найдены в transactions
    result = {category: category_count[category] for category in categories}

    # Выводим информацию о пропущенных операциях по категориям
    if missing_description_count > 0:
        print(f"Пропущено {missing_description_count} операций без 'description'.")

    return result
