from typing import Any, Dict, List, Union


# Функция фильтрует список словарей по ключу.
def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> Union[str, List[Dict[str, Any]]]:
    """Функция фильтрует список словарей по ключу state.

    Аргументы:
    data (list): Список словарей, которые необходимо отфильтровать.
    state (str): Значение ключа state, по которому происходит фильтрация (по умолчанию 'EXECUTED').

    Возвращает:
    filtered_list: Новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    # Проверка на пустой список
    if not data:
        return "Ошибка: передан пустой список."

    filtered_list = []

    for key_value in data:
        # Проверка на тип элемента
        if not isinstance(key_value, dict):
            return "Ошибка: элемент списка должен быть словарем."

        # Добавление элемента в отфильтрованный список, если значение ключа 'state' совпадает
        if key_value.get("state") == state:
            filtered_list.append(key_value)

    # Проверка, не пуст ли список отфильтрованных данных
    if not filtered_list:
        return f"Ошибка: значение '{state}' не найдено для ключа 'state'."

    return filtered_list


# Функция для извлечения определённого слова из списка со словарём
def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по дате.

    Аргументы:
    data (List[Dict[str, Any]]): Список словарей с данными, содержащими поле 'date'.
    reverse (bool): Порядок сортировки (по умолчанию - убывание).

    Возвращает:
    List[Dict[str, Any]]: Отсортированный список словарей.
    """

    # Функция для извлечения даты из словаря
    def get_date(item: Dict[str, Any]) -> str:
        return item.get("date", "0")  # Возвращаем строку "0", если date отсутствует

    # Сортировка списка по дате
    return sorted(data, key=get_date, reverse=reverse)
