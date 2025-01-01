import pytest


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
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2019-05-01T12:00:00.000000",
            "operationAmount": {
                "amount": "500.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод в евро",
            "from": "Счет 11111111111111111111",
            "to": "Счет 22222222222222222222"
        }
    ]
