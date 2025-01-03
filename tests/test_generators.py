import pytest


from src.generators import filter_by_currency, transaction_descriptions


# Тесты с параметризацией функции filter_by_currency
@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [1, 3]),  # Ожидаем, что вернутся транзакции с id 1 и 3
    ("RUB", [2]),     # Ожидаем, что вернется транзакция с id 2
    ("BTC", [4]),     # Ожидаем, что вернется транзакция с id 4
    ("GBP", []),      # Ожидаем, что не будет транзакций
])
def test_filter_by_currency(transactions, currency, expected_ids):
    filtered_transactions = list(filter_by_currency(transactions, currency))
    filtered_ids = [t["id"] for t in filtered_transactions]
    assert filtered_ids == expected_ids


# Тест для пустого списка
def test_empty_list():
    assert list(filter_by_currency([], "USD")) == []


# Тест для списка без соответствующих валютных операций
def test_no_matching_currency():
    transactions = [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "RUB"
                }
            }
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "code": "RUB"
                }
            }
        }
    ]
    assert list(filter_by_currency(transactions, "USD")) == []


def test_filter_by_currency_1():
    """Тестирование функции фильтрации транзакций по валюте."""
    transactions = [
        {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"}
            },
            "description": "Transaction 1"
        },
        {
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "EUR"}
            },
            "description": "Transaction 2"
        },
        {
            "operationAmount": {
                "amount": "150.00",
                "currency": {"code": "USD"}
            },
            "description": "Transaction 3"
        },
        {
            "operationAmount": {
                "amount": "300.00",
                "currency": {"code": "GBP"}
            },
            "description": "Transaction 4"
        }
    ]

    # Тестируем фильтрацию по USD
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["description"] == "Transaction 1"
    assert result[1]["description"] == "Transaction 3"

    # Тестируем фильтрацию по EUR
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 1
    assert result[0]["description"] == "Transaction 2"

    # Тестируем фильтрацию по GBP
    result = list(filter_by_currency(transactions, "GBP"))
    assert len(result) == 1
    assert result[0]["description"] == "Transaction 4"

    # Тестируем фильтрацию по несуществующей валюте
    result = list(filter_by_currency(transactions, "JPY"))
    assert len(result) == 0


def test_empty_transactions():
    """Тестирование функции с пустым списком транзакций."""
    transactions = []
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


# Тесты с параметризацией функции - генератора transaction_descriptions
@pytest.mark.parametrize("transactions_1, expected", [
    ([
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Оплата"},
        {"description": "Оплата не прошла"},
    ], [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Оплата",
        "Оплата не прошла"
    ]),
    ([], []),    # Тест для пустого списка
    ([{"description": "Неизвестная операция"}], ["Неизвестная операция"]),
    # Тест для одной неизвестной операции
    ([{}], ["Неизвестная транзакция"]),    # Тест дял пустого словаря
])
def test_transaction_descriptions(transactions_1, expected):
    descriptions = list(transaction_descriptions(transactions_1))
    assert descriptions == expected
