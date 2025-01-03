from typing import List, Dict, Iterator

def filter_by_currency(transactions: List[Dict[str, Dict[str, str]]], currency: str) -> Iterator[Dict[str, Dict[str, str]]]:
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
