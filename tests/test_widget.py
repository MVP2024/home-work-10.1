import pytest
from src.widget import mask_account_card, get_date


# Тестирование функции mask_account_card
# Фикстура для тестирования
@pytest.fixture
def valid_visa_card():
    return "Visa 1234567812345678"


@pytest.fixture
def valid_mastercard():
    return "MasterCard 1234567812345678"


@pytest.fixture
def valid_account():
    return "Счёт 1234567812345678"


@pytest.fixture
def short_card():
    return "Visa 12345678"  # 8 цифр


@pytest.fixture
def long_card():
    return "Visa 12345678123456789"  # 17 цифр


@pytest.fixture
def invalid_card_chars():
    return "Visa 1234abcd5678efgh"  # Содержит буквы


@pytest.fixture
def empty_card():
    return ""  # Пустая строка


@pytest.fixture
def no_type_card():
    return "1234567812345678"  # Нет типа карты


# Параметризация тестов
@pytest.mark.parametrize(
    "types_requisites, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56 ** **** 5678"),  # Корректный номер карты Visa
        ("MasterCard 1234567812345678", "MasterCard 1234567812345678"),  # Корректный номер MasterCard
        ("Счёт 1234567812345678", "Счёт **5678"),  # Корректный номер счёта
        ("Visa 12345678", "Ошибка: неверно указан номер карты/счёта."),  # Слишком короткий номер
        ("Visa 12345678123456789", "Ошибка: неверно указан номер карты/счёта."),  # Слишком длинный номер
        ("Visa 1234abcd5678efgh", "Ошибка: неверно указан номер карты/счёта."),  # Недопустимые символы
        ("", "Ошибка: входная строка пустая."),  # Пустая строка
        ("1234567812345678", "Ошибка: номер указан без типа карты/счёта."),  # Нет типа карты
        ("UnknownType 1234567812345678", "Ошибка: номер указан без типа карты/счёта."),  # Неизвестный тип
    ],
)
def test_mask_account_card(types_requisites, expected):
    assert mask_account_card(types_requisites) == expected


# Тесты с использованием фикстур
def test_valid_visa_card(valid_visa_card):
    assert mask_account_card(valid_visa_card) == "Visa 1234 56 ** **** 5678"


def test_valid_mastercard(valid_mastercard):
    assert mask_account_card(valid_mastercard) == "MasterCard 1234567812345678"


def test_valid_account(valid_account):
    assert mask_account_card(valid_account) == "Счёт **5678"


def test_short_card(short_card):
    assert mask_account_card(short_card) == "Ошибка: неверно указан номер карты/счёта."


def test_long_card(long_card):
    assert mask_account_card(long_card) == "Ошибка: неверно указан номер карты/счёта."


def test_invalid_card_chars(invalid_card_chars):
    assert mask_account_card(invalid_card_chars) == "Ошибка: неверно указан номер карты/счёта."


def test_empty_card(empty_card):
    assert mask_account_card(empty_card) == "Ошибка: входная строка пустая."


def test_no_type_card(no_type_card):
    assert mask_account_card(no_type_card) == "Ошибка: номер указан без типа карты/счёта."


# Тестирование функции `get_date`
# Фикстуры для тестирования
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


# Параметризация тестов
@pytest.mark.parametrize(
    "data_full, expected",
    [
        ("2023-03-15T12:30:00", "15.03.2023"),  # Корректный случай
        ("2020-02-29T15:45:00", "29.02.2020"),  # Високосный год
        ("2023-01-01T00:00:00", "01.01.2023"),  # Первый день года
        ("2023-12-31T23:59:59", "31.12.2023"),  # Последний день года
        ("2023-13-15T12:30:00", "Ошибка: некорректный месяц."),  # Некорректный месяц
        ("2023-04-31T12:30:00", "Ошибка: некорректный день."),  # Некорректный день
        ("2023-02-29T12:30:00", "Ошибка: некорректный день."),  # Не високосный год
        ("2023/03/15 12:30:00", "Ошибка: неверный формат даты."),  # Неверный формат
        ("", "Ошибка: входная строка пустая."),  # Пустая строка
        ("2023-03-15", "Ошибка: неверный формат даты."),  # Нет времени
        ("2023-03-1aT12:30:00", "Ошибка: дата содержит недопустимые символы."),  # Неверные символы
    ],
)
def test_get_date(data_full, expected):
    assert get_date(data_full) == expected


# Тесты с использованием фикстур
def test_valid_date(valid_date):
    assert get_date(valid_date) == "15.03.2023"


def test_leap_year_date(leap_year_date):
    assert get_date(leap_year_date) == "29.02.2020"


def test_invalid_date_format(invalid_date_format):
    assert get_date(invalid_date_format) == "Ошибка: неверный формат даты."


def test_empty_date(empty_date):
    assert get_date(empty_date) == "Ошибка: входная строка пустая."


def test_no_time_part(no_time_part):
    assert get_date(no_time_part) == "Ошибка: неверный формат даты."


def test_invalid_month(invalid_month):
    assert get_date(invalid_month) == "Ошибка: некорректный месяц."


def test_invalid_day(invalid_day):
    assert get_date(invalid_day) == "Ошибка: некорректный день."


def test_invalid_characters(invalid_characters):
    assert get_date(invalid_characters) == "Ошибка: дата содержит недопустимые символы."
