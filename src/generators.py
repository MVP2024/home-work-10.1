from typing import List, Dict, Any, Iterator


def filter_by_currency(transactions, currency):
    """
    Функция фильтрует транзакции по заданной валюте и возвращает итератор с соответствующими транзакциями.

    :param transactions: Список словарей, представляющих транзакции.
    :param currency_code: Код валюты, по которой необходимо фильтровать транзакции.
    :return: Итератор с транзакциями, соответствующими заданной валюте.
    :raises ValueError: Если transactions не является списком или currency_code не является строкой.
    :raises ValueError: Если transactions пустой или не содержит операций с указанной валютой.
    """
    if not isinstance(transactions, list):
        raise ValueError("transactions должен быть списком.")
    if not isinstance(currency, str):
        raise ValueError("currency_code должен быть строкой.")
    if not transactions:
        raise ValueError("Список transactions не должен быть пустым.")

    filtered_transactions = (
        transaction for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )

    if not any(filtered_transactions):
        raise ValueError(f"Нет транзакций с валютой: {currency}")

    return filtered_transactions
