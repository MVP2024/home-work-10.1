import pytest

from src.masks import get_mask_card_number, get_mask_account


# Тестирование функции `get_mask_card_number`
# Параметризация тестов
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("123456781234", "Ошибка: слишком короткий номер."),
        ("12345678123456789", "Ошибка: слишком длинный номер."),
        ("1234abcd5678efgh", "Ошибка: присутствуют другие символы."),
        ("", "Ошибка: входная строка пустая."),
        ("123456781234567", "Ошибка: слишком короткий номер."),
        ("12345678123456780", "Ошибка: слишком длинный номер."),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


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


# Тестирование функции `get_mask_account`
# Параметризация тестов
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567812345678", "**5678"),
        ("123456781234", "Ошибка: слишком короткий номер."),
        ("12345678123456789", "Ошибка: слишком длинный номер."),
        ("1234abcd5678efgh", "Ошибка: присутствуют другие символы."),
        ("", "Ошибка: входная строка пустая."),
        ("123456781234567", "Ошибка: слишком короткий номер."),
        ("12345678123456780", "Ошибка: слишком длинный номер."),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


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
