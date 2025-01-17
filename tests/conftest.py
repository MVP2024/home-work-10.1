import os

import pytest

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
def transactions():
    return [
        {"id": 1, "operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"amount": "200.00", "currency": {"code": "RUB"}}},
        {"id": 3, "operationAmount": {"amount": "150.00", "currency": {"code": "USD"}}},
        {"id": 4, "operationAmount": {"amount": "250.00", "currency": {"code": "BTC"}}},
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


# Фикстура для тестирования convert_to_rub
@pytest.fixture
def set_api_key():
    """Фикстура для установки тестового API-ключа."""
    os.environ["API_KEY"] = "test_api_key"  # Установите тестовый ключ API
