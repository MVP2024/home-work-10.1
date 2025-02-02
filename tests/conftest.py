import pytest

from src.bank_operations import filter_bank_operations
from src.decorators import log


# Фикстуры для тестирования номера карты
@pytest.fixture
def correct_card():
    return "1234567812345678"


@pytest.fixture
def short_card():
    return "12345678"  # 8 цифр


@pytest.fixture
def long_card():
    return "12345678123456789"  # 17 цифр


@pytest.fixture
def invalid_card_chars():
    return "1234abcd5678efgh"  # Содержит буквы


@pytest.fixture
def empty_card():
    return ""  # Пустая строка


# Фикстуры для тестирования номера счета
@pytest.fixture
def valid_account():
    return "1234567812345678"


@pytest.fixture
def short_account():
    return "12345678"  # 8 цифр


@pytest.fixture
def long_account():
    return "12345678123456789"  # 17 цифр


@pytest.fixture
def invalid_account_chars():
    return "1234abcd5678efgh"  # Содержит буквы


@pytest.fixture
def empty_account():
    return ""  # Пустая строка


# Фикстуры для тестирования `state`
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "PENDING"},
        {"id": 4, "state": None},
        {"id": 5, "state": "EXECUTED"},
    ]


# Фикстуры для тестирования карт
@pytest.fixture
def valid_visa_card():
    return "Visa 1234567812345678"


@pytest.fixture
def valid_mastercard():
    return "MasterCard 1234567812345678"


@pytest.fixture
def correct_account():
    return "Счёт 1234567812345678"


@pytest.fixture
def short_number_card():
    return "Visa 12345678"  # 8 цифр


@pytest.fixture
def long_number_card():
    return "Visa 12345678123456789"  # 17 цифр


@pytest.fixture
def incorrect_card_chars():
    return "Visa 1234abcd5678efgh"  # Содержит буквы


@pytest.fixture
def card_no_data():
    return ""  # Пустая строка


@pytest.fixture
def no_type_card():
    return "1234567812345678"  # Нет типа карты


# Фикстуры для тестирования транзакций
@pytest.fixture
def transactions_3():
    """Фикстура для предоставления тестовых транзакций."""
    return [
        {"id": 1, "operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"amount": "150.00", "currency": {"code": "EUR"}}},
        {"id": 3, "currency_code": "USD", "amount": "200.00"},  # Простая структура
        {"id": 4, "operationAmount": {"amount": "250.00", "currency": {"code": "BTC"}}},
        {"id": 5, "currency_code": "EUR", "amount": "300.00"},  # Простая структура
    ]


# Фикстуры для тестирования описания каждой транзакции
@pytest.fixture
def transactions_1():
    return [
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Оплата"},
        {"description": "Оплата не прошла"},
        {"description": "Неизвестная операция"},
    ]


@pytest.fixture
def empty_transactions():
    return []


# Фикстуры для тестирования генерации номеров карт
@pytest.fixture
def negative_values():
    return [(-1, 5), (0, -5)]


@pytest.fixture
def non_integer_values():
    return [(1.5, 5), (1, "5")]


# Фикстура для тестирования декоратора log
@log()
def add(a, b):
    return a + b


@log()
def divide(a, b):
    return a / b


@log()
def raise_error():
    raise ValueError("This is an error")


# Фикстура для тестирования filter_bank_operations
@pytest.fixture
def transactions_2():
    return [
        {"id": "1", "description": "Перевод с карты на карту"},
        {"id": "2", "description": "Открытие вклада"},
        {"id": "3", "description": "Закрытие вклада"},
        {"id": "4", "description": "Перевод на счет"},
        {"id": "5", "description": "Оплата услуг"},
    ]


def test_filter_by_exact_match(transactions_2):
    result = filter_bank_operations(transactions_2, "Перевод с карты на карту")
    assert len(result) == 1
    assert result[0]["id"] == "1"


# Фикстура для функции count_operations_by_category
def transactions():
    """Фикстура для предоставления тестовых транзакций."""
    return [
        {"id": 1, "description": "Перевод с карты на карту"},
        {"id": 2, "description": "Оплата услуг"},
        {"id": 3, "description": "Перевод на счет"},
        {"id": 4, "description": "Закрытие вклада"},
        {"id": 5, "description": "Перевод с карты на карту"},
    ]


@pytest.fixture
def categories():
    """Фикстура для предоставления тестовых категорий."""
    return ["Перевод", "Оплата", "Закрытие"]
