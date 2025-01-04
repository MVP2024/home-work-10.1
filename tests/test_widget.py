import pytest

from src.widget import get_date, mask_account_card


# Запуск тестов
if __name__ == "__main__":
    pytest.main()


# Тестирование функции mask_account_card
# Параметризация тестов для mask_account_card
@pytest.mark.parametrize(
    "types_requisites, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56 ** **** 5678"),
        ("MasterCard 1234567812345678", "MasterCard 1234567812345678"),
        ("Счёт 1234567812345678", "Счёт **5678"),
        ("Visa 12345678", "Ошибка: неверно указан номер карты/счёта."),
        ("Visa 12345678123456789", "Ошибка: неверно указан номер карты/счёта."),
        ("Visa 1234abcd5678efgh", "Ошибка: неверно указан номер карты/счёта."),
        ("", "Ошибка: входная строка пустая."),
        ("1234567812345678", "Ошибка: номер указан без типа карты/счёта."),
        ("UnknownType 1234567812345678", "Ошибка: номер указан без типа карты/счёта."),
    ],
)
def test_mask_account_card(types_requisites, expected):
    assert mask_account_card(types_requisites) == expected


# Тесты с использованием фикстур
def test_valid_visa_card(valid_visa_card):
    assert mask_account_card(valid_visa_card) == "Visa 1234 56 ** **** 5678"


def test_valid_mastercard(valid_mastercard):
    assert mask_account_card(valid_mastercard) == "MasterCard 1234567812345678"


def test_correct_account(correct_account):
    assert mask_account_card(correct_account) == "Счёт **5678"


def test_short_number_card(short_number_card):
    assert mask_account_card(short_number_card) == "Ошибка: неверно указан номер карты/счёта."


def test_long_number_card(long_number_card):
    assert mask_account_card(long_number_card) == "Ошибка: неверно указан номер карты/счёта."


def test_incorrect_card_chars(incorrect_card_chars):
    assert mask_account_card(incorrect_card_chars) == "Ошибка: неверно указан номер карты/счёта."


def test_card_no_data(card_no_data):
    assert mask_account_card(card_no_data) == "Ошибка: входная строка пустая."


def test_no_type_card(no_type_card):
    assert mask_account_card(no_type_card) == "Ошибка: номер указан без типа карты/счёта."


# тестирование функции get_date
# Параметризация тестов для get_date
@pytest.mark.parametrize(
    "data_full, expected",
    [
        ("2023-03-15T12:30:00", "15.03.2023"),
        ("2020-02-29T15:45:00", "29.02.2020"),
        ("2023-01-01T00:00:00", "01.01.2023"),
        ("2023-12-31T23:59:59", "31.12.2023"),
        ("2023-13-15T12:30:00", "Ошибка: некорректный месяц."),
        ("2023-04-31T12:30:00", "Ошибка: некорректный день."),
        ("2023-02-29T12:30:00", "Ошибка: некорректный день."),
        ("2023/03/15 12:30:00", "Ошибка: неверный формат даты."),
        ("", "Ошибка: входная строка пустая."),
        ("2023-03-15", "Ошибка: неверный формат даты."),
        ("2023-03-1aT12:30:00", "Ошибка: дата содержит недопустимые символы."),
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
