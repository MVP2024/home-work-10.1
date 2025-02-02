from typing import Any, Dict, List, Union

from src.decorators import log


@log("mylog.txt")
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
        # Проверяем наличие ключа "state", если его нет - просто пропускаем элемент
        if "state" in item and item["state"] is not None and item["state"] == state:
            filtered_data.append(item)

    if not filtered_data:
        return f"Ошибка: значение '{state}' не найдено для ключа 'state'."

    return filtered_data


@log("mylog.txt")
def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по значению ключа 'date'.

    Функция фильтрует записи, исключая те, у которых отсутствует ключ 'date'
    или значение этого ключа пустое. Затем, отсортирует оставшиеся записи
    по значению ключа 'date'.

    :param data: Список словарей, где каждый словарь может содержать ключ 'date'.
    :param reverse: Если True, сортировка будет выполнена в обратном порядке (по умолчанию).
    :return: Новый отсортированный список словарей.
    """

    def get_date(item: Dict[str, Any]) -> str:
        """
        Извлекает значение ключа 'date' из словаря.

        Если ключ 'date' отсутствует или его значение пустое, возвращает пустую строку.

        :param item: Словарь, из которого нужно извлечь значение ключа 'date'.
        :return: Значение ключа 'date' или пустая строка.
        """
        # Проверка наличия ключа "date"
        if "date" not in item or not item["date"]:
            return ""  # Возвращаем пустую строку для отсутствующих или пустых значений

        return item["date"]

    # Фильтруем данные, исключая записи с отсутствующими датами
    filtered_data = [item for item in data if "date" in item and item["date"]]

    # Сортируем отфильтрованные данные
    return sorted(filtered_data, key=get_date, reverse=reverse)
