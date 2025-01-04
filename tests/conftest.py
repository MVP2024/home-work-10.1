import pytest


# Запуск тестов
if __name__ == "__main__":
    pytest.main()


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


# Фикстуры для тестирования `date`
@pytest.fixture
def data_sample():
    return [
        {"date": "2023-01-01"},
        {"date": "2022-12-31"},
        {"date": "2023-01-02"},
        {"date": "2022-12-30"},
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


# Фикстуры для тестирования дат
@pytest.fixture
def valid_date():
    return "2023-03-15T12:30:00"  # Корректная дата


@pytest.fixture
def leap_year_date():
    return "2020-02-29T15:45:00"  # Корректная дата високосного года


@pytest.fixture
def invalid_date_format():
    return "2023/03/15 12:30:00"  # Неверный формат даты


@pytest.fixture
def empty_date():
    return ""  # Пустая строка


@pytest.fixture
def no_time_part():
    return "2023-03-15"  # Нет времени


@pytest.fixture
def invalid_month():
    return "2023-13-15T12:30:00"  # Некорректный месяц


@pytest.fixture
def invalid_day():
    return "2023-04-31T12:30:00"  # Некорректный день


@pytest.fixture
def invalid_characters():
    return "2023-03-1aT12:30:00"  # Неверные символы в дате


# Фикстуры для тестирования транзакций
@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "USD"
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
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "150.00",
                "currency": {
                    "code": "USD"
                }
            }
        },
        {
            "id": 4,
            "operationAmount": {
                "amount": "250.00",
                "currency": {
                    "code": "BTC"
                }
            }
        }
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
def card_range():
    return 1000, 1005
