import pytest

from src.masks import get_mask_account, get_mask_card_number  # Импортируем функции


# Тестирование функции `get_mask_card_number`
# Параметризация тестов
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("123456781234", "Ошибка: слишком короткий номер карты."),
        ("12345678123456789", "Ошибка: слишком длинный номер карты."),
        ("1234abcd5678efgh", "Ошибка: присутствуют другие символы в номера карты."),
        ("", "Ошибка: входная строка пустая."),
        ("123456781234567", "Ошибка: слишком короткий номер карты."),
        ("12345678123456780", "Ошибка: слишком длинный номер карты."),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тесты с использованием фикстур для карт
def test_correct_card(correct_card):
    assert get_mask_card_number(correct_card) == "1234 56** **** 5678"


def test_short_card(short_card):
    assert get_mask_card_number(short_card) == "Ошибка: слишком короткий номер карты."


def test_long_card(long_card):
    assert get_mask_card_number(long_card) == "Ошибка: слишком длинный номер карты."


def test_invalid_card_chars(invalid_card_chars):
    assert get_mask_card_number(invalid_card_chars) == "Ошибка: присутствуют другие символы в номере карты."


def test_empty_card(empty_card):
    assert get_mask_card_number(empty_card) == "Ошибка: входная строка пустая."


# Тестирование функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567812345678", "**5678"),
        ("123456781234", "Ошибка: слишком короткий номер счёта."),
        ("12345678123456789", "Ошибка: слишком длинный номер счёта."),
        ("1234abcd5678efgh", "Ошибка: присутствуют другие символы в счёте."),
        ("", "Ошибка: входная строка пустая."),
        ("123456781234567", "Ошибка: слишком короткий номер счёта."),
        ("12345678123456780", "Ошибка: слишком длинный номер счёта."),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


# Тесты с использованием фикстур для счетов
def test_valid_account(valid_account):
    assert get_mask_account(valid_account) == "**5678"


def test_short_account(short_account):
    assert get_mask_account(short_account) == "Ошибка: слишком короткий номер счёта."


def test_long_account(long_account):
    assert get_mask_account(long_account) == "Ошибка: слишком длинный номер счёта."


def test_invalid_account_chars(invalid_account_chars):
    assert get_mask_account(invalid_account_chars) == "Ошибка: присутствуют другие символы в счёте."


def test_empty_account(empty_account):
    assert get_mask_account(empty_account) == "Ошибка: входная строка пустая."
