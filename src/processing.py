from typing import Any, Dict, List


# Функция фильтрует список словарей по ключу.
def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует список словарей по ключу state.

    Аргументы:
    list_of_dictionaries (list): Список словарей, которые необходимо отфильтровать.
    State (str): Значение ключа state, по которому происходит фильтрация (по умолчанию 'EXECUTED').

    Возвращает:
    filtered_list: Новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    filtered_list = []
    for key_value in data:
        if key_value.get("state", "Неправильно введён ключ") == state:
            filtered_list.append(key_value)

    return filtered_list


# Функция для извлечения определённого слова из списка со словарём
def get_data(data) -> str:
    """Извлекаем date из словаря с помощью get"""

    return data.get("date", 0)


# Сортировка списка по дате с помощью функции get_date.
def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по дате.

    Аргументы:
    data (list): Список словарей с данными.
    reverse (bool): Порядок сортировки (по умолчанию - убывание).

    Возвращает:
    list: Отсортированный список словарей.
    """

    return sorted(data, key=get_data, reverse=reverse)
