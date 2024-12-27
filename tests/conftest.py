import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


# Тестирование функции `get_mask_account`
# Фикстура для тестирования
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


# Тесты с использованием фикстур
def test_valid_account(valid_account):
    assert get_mask_account(valid_account) == "**5678"


def test_short_account(short_account):
    assert get_mask_account(short_account) == "Ошибка: слишком короткий номер."


def test_long_account(long_account):
    assert get_mask_account(long_account) == "Ошибка: слишком длинный номер."


def test_invalid_account_chars(invalid_account_chars):
    assert get_mask_account(invalid_account_chars) == "Ошибка: присутствуют другие символы."


def test_empty_account(empty_account):
    assert get_mask_account(empty_account) == "Ошибка: входная строка пустая."


# Тестирование функции `get_mask_card_number`
# Фикстуры для тестирования
@pytest.fixture
def valid_card():
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


# Тесты с использованием фикстур.
def test_valid_card(valid_card):
    assert get_mask_card_number(valid_card) == "1234 56** **** 5678"


def test_short_card(short_card):
    assert get_mask_card_number(short_card) == "Ошибка: слишком короткий номер."


def test_long_card(long_card):
    assert get_mask_card_number(long_card) == "Ошибка: слишком длинный номер."


def test_invalid_card_chars(invalid_card_chars):
    assert get_mask_card_number(invalid_card_chars) == "Ошибка: присутствуют другие символы."


def test_empty_card(empty_card):
    assert get_mask_card_number(empty_card) == "Ошибка: входная строка пустая."


# Тестирование функции `filter_by_state`
# Фикстуры для тестирования
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "PENDING"},
        {"id": 4, "state": None},
        {"id": 5, "state": "EXECUTED"},
    ]


# Тесты с использованием фикстур.
def test_empty_data():
    assert filter_by_state([], "EXECUTED") == "Ошибка: входная строка пустая."


def test_missing_state_key():
    assert filter_by_state([{"id": 1}], "EXECUTED") == "Ошибка: такого ключа нет."


def test_none_state_value():
    assert (
        filter_by_state([{"id": 1, "state": None}], "EXECUTED")
        == "Ошибка: значение 'EXECUTED' не найдено для ключа 'state'."
    )


# Тестирование функции `sort_by_date`
# Фикстуры для тестирования
@pytest.fixture
def data_sample():
    return [
        {"date": "2023-01-01"},
        {"date": "2022-12-31"},
        {"date": "2023-01-02"},
        {"date": "2022-12-30"},
    ]


# Тесты с использованием фикстур.
def test_empty_list():
    with pytest.raises(ValueError, match="Ошибка: передан пустой список."):
        sort_by_date([])


def test_missing_date_key():
    with pytest.raises(ValueError, match="Ошибка: отсутствует ключ 'date'"):
        sort_by_date([{"not_date": "2023-01-01"}])


def test_none_date_value():
    with pytest.raises(ValueError, match="Ошибка: значение по ключу 'date'"):
        sort_by_date([{"date": None}])


# Тестирование функции mask_account_card
# Фикстура для тестирования
@pytest.fixture
def valid_visa_card():
    return "Visa 1234567812345678"


@pytest.fixture
def valid_mastercard():
    return "MasterCard 1234567812345678"


@pytest.fixture
def valid_account_1():
    return "Счёт 1234567812345678"


@pytest.fixture
def short_card_1():
    return "Visa 12345678"  # 8 цифр


@pytest.fixture
def long_card_1():
    return "Visa 12345678123456789"  # 17 цифр


@pytest.fixture
def invalid_card_chars_1():
    return "Visa 1234abcd5678efgh"  # Содержит буквы


@pytest.fixture
def empty_card_1():
    return ""  # Пустая строка


@pytest.fixture
def no_type_card():
    return "1234567812345678"  # Нет типа карты


# Тесты с использованием фикстур
def test_valid_visa_card(valid_visa_card):
    assert mask_account_card(valid_visa_card) == "Visa 1234 56 ** **** 5678"


def test_valid_mastercard(valid_mastercard):
    assert mask_account_card(valid_mastercard) == "MasterCard 1234567812345678"


def test_valid_account_1():
    valid_account = "Счёт 1234567812345678"  # Передаем тип и номер
    assert mask_account_card(valid_account) == "Счёт **5678"


def test_short_card_1(short_card):
    assert mask_account_card(short_card) == "Ошибка: неверно указан номер карты/счёта."


def test_long_card_1(long_card):
    assert mask_account_card(long_card) == "Ошибка: неверно указан номер карты/счёта."


def test_invalid_card_chars_1(invalid_card_chars):
    assert mask_account_card(invalid_card_chars) == "Ошибка: неверно указан номер карты/счёта."


def test_empty_card_1(empty_card):
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
