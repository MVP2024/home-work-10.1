from typing import List, Dict, Iterator, Any


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
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который принимает список транзакций и возвращает описание каждой операции."""
    for transaction in transactions:
        # Извлекаем описание транзакций
        description = transaction.get("description", "Неизвестная транзакция")
        yield description


def card_number_generator(start: int, end: int):
    """Генератор для создания номеров банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        # Преобразуем число в строку
        card_number = str(number)
        # Дополняем нуями слева до 16 символов
        while len(card_number) < 16:
            card_number = '0' + card_number
        # Форматируем строку в нужном виде
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
