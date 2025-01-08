from typing import Union

from src.decorators import log


@log("mylog.txt")
def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает замаскированный номер"""

    # Проверяем, является ли строка пустой
    if not card_number:
        return "Ошибка: входная строка пустая."

    # Проверяем длину номера карты
    if len(card_number) < 16:
        return "Ошибка: слишком короткий номер."
    elif len(card_number) > 16:
        return "Ошибка: слишком длинный номер."

    # Проверяем, если в номере карты присутствуют кроме цифр, другие символы
    if not card_number.isdigit():
        return "Ошибка: присутствуют другие символы."

    # Маскируем номер карты
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

    # Возвращаем замаскированный номер в формате XXXX XX** **** XXXX.
    return masked_card_number


@log("mylog.txt")
def get_mask_account(account_number: Union[str]) -> Union[str, ValueError]:
    """Функция принимает на вход номер счёта и возвращает замаскированный счёт"""

    # Проверяем, является ли строка пустой
    if not account_number:
        return "Ошибка: входная строка пустая."

    # Проверяем длину номера счёта
    if len(account_number) < 16:
        return "Ошибка: слишком короткий номер."
    elif len(account_number) > 16:
        return "Ошибка: слишком длинный номер."

    # Проверяем, если в номере счёта присутствуют кроме цифр, другие символы
    if not account_number.isdigit():
        return "Ошибка: присутствуют другие символы."

    # Маскируем номер счёта
    masked_account = "**" + account_number[-4:]

    # Возвращаем замаскированный номер
    return masked_account
