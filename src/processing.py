from typing import Any, Dict, List


# Функция фильтрует список словарей по ключу.
def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]] | KeyError:
    """Функция фильтрует список словарей по ключу state."""
    try:
        if not data:
            raise ValueError("Нет данных")
        filtered_list: list[dict[str, Any]] = []
        for key_value in data:
            if "state" not in key_value:
                raise KeyError("Ключ 'state' не найден.")
            if key_value["state"] == state:
                filtered_list.append(key_value)

        # возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует значению
        return filtered_list

    except KeyError as ve:
        return ve


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
