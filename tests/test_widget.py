import pytest

from src.widget import get_date, mask_account_card


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


def test_mask_account_card_valid():
    assert mask_account_card("Visa 1234567812345678") == "Visa 1234 56 ** **** 5678"
    assert mask_account_card("Счёт 1234567812345678") == "Счёт **5678"


def test_mask_account_card_empty():
    assert mask_account_card("") == "Ошибка: входная строка пустая."


def test_mask_account_card_invalid_characters():
    assert mask_account_card("Visa 1234-5678-1234-5678") == "Ошибка: неверно указан номер карты/счёта."


def test_mask_account_card_no_number():
    assert mask_account_card("Visa") == "Ошибка: тип 'visa' указан без номера."


def test_mask_account_card_too_short():
    assert mask_account_card("Visa 12345") == "Ошибка: неверно указан номер карты/счёта."


def test_mask_account_card_too_long():
    assert mask_account_card("Visa 123456781234567890") == "Ошибка: неверно указан номер карты/счёта."


def test_mask_account_card_no_type():
    assert mask_account_card("1234567812345678") == "Ошибка: номер указан без типа карты/счёта."


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


# Дополнительные тесты
def test_valid_date():
    assert get_date("2023-03-15T12:00:00") == "15.03.2023"


def test_leap_year_date():
    assert get_date("2020-02-29T15:45:00") == "29.02.2020"


def test_invalid_date_format():
    assert get_date("2023-03-15 12:00:00") == "Ошибка: неверный формат даты."


def test_empty_date():
    assert get_date("") == "Ошибка: входная строка пустая."


def test_no_time_part():
    assert get_date("2023-03-15") == "Ошибка: неверный формат даты."


def test_invalid_month():
    assert get_date("2023-13-15T12:00:00") == "Ошибка: некорректный месяц."


def test_invalid_day():
    assert get_date("2023-02-30T12:00:00") == "Ошибка: некорректный день."


def test_invalid_characters():
    assert get_date("2023-XX-15T12:00:XX") == "Ошибка: дата содержит недопустимые символы."


def test_incorrect_format_no_t():
    assert get_date("2023-03-15 12:00:00") == "Ошибка: неверный формат даты."


def test_incorrect_format_t_not_found():
    assert get_date("25:00:00T2023-03-15") == "Ошибка: дата содержит недопустимые символы."


def test_invalid_time():
    assert get_date("0000-00-00T25:00:00") == "Ошибка: некорректный месяц."


def test_invalid_time_characters():
    assert get_date("2023-03-XXT12:00:XX") == "Ошибка: дата содержит недопустимые символы."


def test_valid_date_with_seconds():
    assert get_date("2023-03-15T12:30:45") == "15.03.2023"


def test_valid_date_with_zero_padded():
    assert get_date("2023-03-01T12:00:00") == "01.03.2023"


def test_valid_date_with_time_edge_case():
    assert get_date("2023-03-15T00:00:00") == "15.03.2023"


@pytest.mark.parametrize(
    "data_full, expected",
    [
        # Тест на неверный формат даты (не 3 части)
        ("2023-03", "Ошибка: неверный формат даты."),
        ("2023-03-15-12:30:00", "Ошибка: неверный формат даты."),
        ("2023-03-15T12:30:00Z", "Ошибка: дата содержит недопустимые символы."),
        # Тест на нецифровые символы в частях даты
        ("2023-0a-15T12:30:00", "Ошибка: дата содержит недопустимые символы."),
        ("2023-03-xxT12:30:00", "Ошибка: дата содержит недопустимые символы."),
        ("2023-03-15T12:30:XX", "15.03.2023"),
        # Тест на некорректный день
        ("2023-03-32T12:30:00", "Ошибка: некорректный день."),
        ("2023-04-31T12:30:00", "Ошибка: некорректный день."),
        ("2023-02-30T12:30:00", "Ошибка: некорректный день."),
        ("2023-02-29T12:30:00", "Ошибка: некорректный день."),  # не високосный год
    ],
)
def test_get_date_invalid_formats(data_full, expected):
    assert get_date(data_full) == expected


@pytest.mark.parametrize(
    "data_full, expected",
    [
        # Тест на неверный формат даты (не 3 части)
        ("2023-03", "Ошибка: неверный формат даты."),
        ("2023-03-15-12:30:00", "Ошибка: неверный формат даты."),
        ("2023-03-15T12:30:00Z", "Ошибка: дата содержит недопустимые символы."),
        ("2023-03-15T", "15.03.2023"),
        ("2023--03-15T12:30:00", "Ошибка: неверный формат даты."),
    ],
)
def test_get_date_invalid_format(data_full, expected):
    assert get_date(data_full) == expected


@pytest.mark.parametrize(
    "data_full, expected",
    [
        # Тест на некорректный день в феврале для не високосного года
        ("2023-02-29T12:30:00", "Ошибка: некорректный день."),
        ("2023-02-30T12:30:00", "Ошибка: некорректный день."),
        # Тест на некорректный день в феврале для високосного года
        ("2024-02-30T12:30:00", "Ошибка: некорректный день."),
        # Тест на корректный день в феврале для високосного года
        ("2024-02-29T12:30:00", "29.02.2024"),
        # Тест на корректный день в феврале для невисокосного года
        ("2023-02-28T12:30:00", "28.02.2023"),
    ],
)
def test_get_date_february_days(data_full, expected):
    assert get_date(data_full) == expected
