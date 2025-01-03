import pytest


from src.generators import filter_by_currency


# Тесты с параметризацией функции filter_by_currency
# Тесты с параметризацией
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
