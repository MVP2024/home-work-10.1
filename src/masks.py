from typing import Union, Any


def get_mask_card_number(card_number: Union[str]) -> str | ValueError:
    try:
        """Функция принимает на вход номер карты и возвращает замаскированный номер"""

        # проверяет если в номере карты не 16 символов, то возвращает ошибку.
        if len(card_number) > 16:
            raise ValueError("Ошибка: Слишком длинный номер карты.")
        elif len(card_number) < 16:
            raise ValueError("Ошибка: Слишком короткий номер карты.")

        # если в номере карты присутствуют кроме цифр, другие символы, то возвращает ошибку.
        for char in card_number:
            if not char.isdigit():
                raise ValueError("Ошибка: Присутствуют другие символы в номере карты")

        # маскирует номер карты.
        masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]

        # возвращаем замаскированный номер в формате XXXX XX** **** XXXX.
        return masked_card_number

    except ValueError as ve:
        return ve


def get_mask_account(account_number: Union[str]) -> str | ValueError | Any:
    try:
        """Функция принимает на вход номер счёта и возвращает замаскированный счёт"""
        # проверяем если в номере счёта присутствуют вместо цифр другие символы
        # и если длинна цифр не равна 16, то возвращает ошибку.
        if not account_number.isdigit():
            raise ValueError("Ошибка: Присутствуют другие символы в номере счёта.")
        elif len(account_number) > 16:
            raise ValueError("Ошибка: Слишком длинный номер счёта.")
        elif len(account_number) < 16:
            raise ValueError("Ошибка: Номер карты слишком короткий.")

        # маскируем номер счёта
        masked_account: str = "**" + account_number[-4:]

        # возвращаем замаскированный номер.
        return masked_account

    except ValueError as ve:
        return ve
