from typing import Union, Any


def mask_account_card(types_requisites: Union[str]) -> str | ValueError | Any:
    try:
        """Функция принимает на вход вид и номер карты или счёта с номером"""

        # создаём переменные-списки для букв и цифр из аргумента.
        card_type = []
        card_number = []

        # если есть буквы и пробелы, то добавляем в card_type и переводим в нижний регистр.
        for char in types_requisites:
            if char.isalpha() or char.isspace():
                card_type.append(char.lower())

            # если есть цифры, то добавляем в card_number.
            elif char.isdigit():
                card_number.append(char)

            # если элементы не цифры, то возникает ошибка.
            elif not char.isdigit():
                raise ValueError("Ошибка: Присутствуют другие символы в номере карты.")
            else:
                raise ValueError("Ошибка: проверьте правильность номера карты")

        # если номер карты или счёта больше 16 символов, то возникнет ошибка.
        if len(card_number) > 16:
            raise ValueError("Ошибка: Слишком длинный номер карты")

        # если номер карты меньше 16 символов, то возникнет ошибка.
        elif len(card_number) < 16:
            raise ValueError("Ошибка: Номер карты короткий")

        card_type_str = "".join(card_type)
        card_number_str = "".join(card_number)

        # сверяет, есть ли слова "счет" или "счёт" в объединённой строке "card_type_str".
        if "счет" in card_type_str or "счёт" in card_type_str:

            # возвращаем копию строки со словами с заглавными буквами методом "capitalize()".
            card_type_str = card_type_str.capitalize()

            # маска номера счёта.
            masked_card_number = "Счет **" + card_number_str[-4:]

        # с помощью функции "any()" ищем определённый объект в итерируемой строке "card_type_str".
        elif any(word in card_type_str for word in ["visa", "maestro", "mastercard", "union"]):

            # объединяем слова с заглавными буквами и разделяем методом "split()".
            card_type_str = " ".join(word.capitalize() for word in card_type_str.split())

            # маскируем номер карты.
            masked_card_number = card_type_str + " " + card_number_str[:-12] + " " + "** **** " + card_number_str[-4:]

        # возвращает название и замаскированный номер карты или счёта.
        return masked_card_number
    except ValueError as ve:
        return ve


def get_date(data_full: Union[str]) -> str | ValueError | Any:
    """Функция, которая принимает на вход строку с датой в формате

    "2024-03-11T02:26:18.671407"""
    try:
        date_list = data_full.split("T")[0].split("-")
        day = date_list[2]
        month = date_list[1]
        year = date_list[0]

        # возвращает строку с датой в формате ДД.ММ.ГГГГ
        return f"{day}.{month}.{year}"

        # при неправильном формате возвращает ошибку.
    except ValueError as ve:
        return ve
