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
