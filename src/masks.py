from typing import Union, Any


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает замаскированный номер"""

    # проверяет если в номере карты не 16 символов, то возвращает ошибку.
    if len(card_number) != 16:
        return "Ошибка: Некорректная длина номера карты"

    # если в номере карты присутствуют кроме цифр, другие символы, то возвращает ошибку.
    for char in card_number:
        if not char.isdigit():
            return "Ошибка: Посторонние символы в номере карты"

    # маскирует номер карты.
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]

    # возвращаем замаскированный номер в формате XXXX XX** **** XXXX.
    return masked_card_number


def get_mask_account(account_number: Union[str]) -> str | ValueError | Any:
    """Функция принимает на вход номер счёта и возвращает замаскированный счёт"""
    try:

        # проверяем если в номере счёта присутствуют вместо цифр другие символы
        # и если длинна цифр не равна 16, то возвращает ошибку.
        if not account_number.isdigit() or len(account_number) != 16:
            raise ValueError("Ошибка: Неправильный номер счёта")

        # маскируем номер счёта
        masked_account = "**" + account_number[-4:]

        # возвращаем замаскированный номер.
        return masked_account
    except ValueError as ve:
        return ve
