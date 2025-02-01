from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.

    :param transactions: Список словарей с транзакциями.
    :param currency: Валюта, по которой нужно фильтровать транзакции.
    :return: Итератор, выдающий транзакции заданной валюты.
    """
    for transaction in transactions:
        # Проверяем, соответствует ли валюта
        # Сначала проверяем более сложную структуру
        operation_amount = transaction.get("operationAmount")
        if operation_amount:
            if operation_amount.get("currency", {}).get("code") == currency:
                yield transaction
        # Затем проверяем простую структуру
        elif transaction.get("currency_code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который принимает список транзакций и возвращает описание каждой операции."""
    for transaction in transactions:
        # Извлекаем описание транзакций
        description = transaction.get("description", "Неизвестная транзакция")
        yield description


def card_number_generator(start, stop):
    """Генератор для создания номеров банковских карт в формате XXXX XXXX XXXX XXXX."""

    # Проверка на целые значения
    if type(start) is not int or type(stop) is not int:
        raise TypeError("start и stop должны быть целыми числами")

    # Проверка на отрицательные значения
    if start < 0 or stop < 0:
        raise ValueError("start и stop не должны быть отрицательными числами")

    # Проверка на диапазон
    if start > stop:
        raise ValueError("значение start должно быть меньше или равно значению stop")

    for number in range(start, stop + 1):
        # Преобразуем число в строку
        card_number = str(number)
        # Дополняем нулями слева до 16 символов
        while len(card_number) < 16:
            card_number = "0" + card_number
        # Форматируем строку в нужном виде
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
