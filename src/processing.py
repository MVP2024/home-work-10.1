from typing import Any, Dict, List, Union


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> Union[str, List[Dict[str, Any]]]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state', по которому выполняется фильтрация.
    :return: Новый список словарей, соответствующих заданному состоянию.
    """
    if not data:
        return "Ошибка: входная строка пустая."

    filtered_data = []
    for item in data:
        if "state" not in item:
            return "Ошибка: такого ключа нет."
        # Не добавляем в filtered_data, если значение None
        if item["state"] is not None and item["state"] == state:
            filtered_data.append(item)

    if not filtered_data:
        return f"Ошибка: значение '{state}' не найдено для ключа 'state'."

    return filtered_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по дате.

    Аргументы:
    data (list): Список словарей с данными.
    reverse (bool): Порядок сортировки (по умолчанию - убывание).

    Возвращает:
    list: Отсортированный список словарей.

    Исключения:
    ValueError: Если список пуст или если в словаре отсутствует ключ "date" или значение по этому ключу.
    """

    # Проверка на пустой список
    if not data:
        raise ValueError("Ошибка: передан пустой список.")

    # Функция для извлечения даты из словаря
    def get_date(item: Dict[str, Any]) -> str:
        # Проверка на наличие ключа "date"
        if "date" not in item:
            raise ValueError(f"Ошибка: отсутствует ключ 'date' в словаре {item}.")

        date_value = item["date"]

        # Проверка на наличие значения по ключу "date"
        if date_value is None or date_value == "":
            raise ValueError(f"Ошибка: значение по ключу 'date' в словаре {item} отсутствует.")

        return date_value

    return sorted(data, key=get_date, reverse=reverse)
