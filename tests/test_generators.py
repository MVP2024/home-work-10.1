import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тестирование функции filter_by_currency
# Тесты с параметризацией функции filter_by_currency
@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),  # Ожидаем, что вернутся транзакции с id 1 и 3
        ("RUB", [2]),  # Ожидаем, что вернется транзакция с id 2
        ("BTC", [4]),  # Ожидаем, что вернется транзакция с id 4
        ("GBP", []),  # Ожидаем, что не будет транзакций
    ],
)
def test_filter_by_currency(transactions, currency, expected_ids):
    filtered_transactions = list(filter_by_currency(transactions, currency))
    filtered_ids = [t["id"] for t in filtered_transactions]
    assert filtered_ids == expected_ids


# Тест для пустого списка
def test_empty_list():
    assert list(filter_by_currency([], "USD")) == []


# Тест для проверки длины списка
def test_transactions(transactions):
    assert len(transactions) > 0


# Тест для списка без соответствующих транзакций с заданной валютой
def test_no_matching_currency():
    transactions = [
        {"id": 1, "operationAmount": {"amount": "100.00", "currency": {"code": "RUB"}}},
        {"id": 2, "operationAmount": {"amount": "200.00", "currency": {"code": "RUB"}}},
    ]
    assert list(filter_by_currency(transactions, "USD")) == []


def test_filter_by_currency_1():
    """Тестирование функции фильтрации транзакций по существующей валюте."""
    transactions = [
        {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}, "description": "Transaction 1"},
        {"operationAmount": {"amount": "200.00", "currency": {"code": "EUR"}}, "description": "Transaction 2"},
        {"operationAmount": {"amount": "150.00", "currency": {"code": "USD"}}, "description": "Transaction 3"},
        {"operationAmount": {"amount": "300.00", "currency": {"code": "GBP"}}, "description": "Transaction 4"},
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


# Тестируем с некорректными данными
def test_incorrect_data():
    transactions = [
        {"id": 1, "operationAmount": {"amount": "100.00", "currency": {}}},
        {"id": 2, "operationAmount": {"amount": "200.00", "currency": {"code": "RUB"}}},
        {"id": 3},  # Отсутствует ключ operationAmount
        {"id": 4, "operationAmount": {"amount": "150.00"}},  # Отсутствует информация о валюте
    ]
    filtered_transactions = list(filter_by_currency(transactions, "USD"))
    assert filtered_transactions == []  # Ожидаем, что не будет транзакций с USD


# Тесты с параметризацией функции - генератора transaction_descriptions
@pytest.mark.parametrize(
    "transactions_1, expected",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Оплата"},
                {"description": "Оплата не прошла"},
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Оплата",
                "Оплата не прошла",
            ],
        ),
        ([], []),  # Тест для пустого списка
        ([{"description": "Неизвестная операция"}], ["Неизвестная операция"]),
        # Тест для одной неизвестной операции
        ([{}], ["Неизвестная транзакция"]),  # Тест дял пустого словаря
    ],
)
def test_transaction_descriptions(transactions_1, expected):
    descriptions = list(transaction_descriptions(transactions_1))
    assert descriptions == expected


# Предполагаем, что функция card_number_generator уже определена
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1000,
            1005,
            [
                "0000 0000 0000 1000",
                "0000 0000 0000 1001",
                "0000 0000 0000 1002",
                "0000 0000 0000 1003",
                "0000 0000 0000 1004",
                "0000 0000 0000 1005",
            ],
        ),
        (
            2000,
            2002,
            [
                "0000 0000 0000 2000",
                "0000 0000 0000 2001",
                "0000 0000 0000 2002",
            ],
        ),
        (
            0,
            5,
            [
                "0000 0000 0000 0000",
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    """Тестирует генератор номеров карт на корректность выдачи номеров."""
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == expected


def test_card_number_generator_edge_cases():
    """Тестирует крайние значения диапазона."""
    start, stop = 0, 5
    generated_numbers = list(card_number_generator(start, stop))

    # Проверяем, что длина сгенерированных номеров соответствует ожидаемой
    assert len(generated_numbers) == (stop - start + 1)

    # Проверяем, что сгенерированные номера соответствуют ожидаемым значениями
    expected_numbers = []
    for i in range(start, stop + 1):
        card_number = str(i)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        expected_numbers.append(formatted_number)

    assert generated_numbers == expected_numbers


def test_card_number_format():
    """Проверяет форматирование номеров карт."""
    start, stop = 1000, 1005
    for number in card_number_generator(start, stop):
        parts = number.split(" ")
        assert len(parts) == 4
        for part in parts:
            assert len(part) == 4


@pytest.mark.parametrize("start, stop", [(5, 1)])
def test_card_number_generator_invalid_range(start, stop):
    with pytest.raises(ValueError, match="значение start должно быть меньше или равно значению stop"):
        list(card_number_generator(start, stop))


@pytest.mark.parametrize("start, stop", [(-1, 5), (0, -5)])
def test_card_number_generator_negative_values(start, stop):
    with pytest.raises(ValueError, match="start и stop не должны быть отрицательными числами"):
        list(card_number_generator(start, stop))


@pytest.mark.parametrize("start, stop", [(1.5, 5), (1, "5")])
def test_card_number_generator_non_integer_values(start, stop):
    with pytest.raises(TypeError, match="start и stop должны быть целыми числами"):
        list(card_number_generator(start, stop))
