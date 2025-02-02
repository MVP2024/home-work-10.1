from typing import Union

from src.decorators import log


@log("mylog.txt")
def mask_account_card(types_requisites: Union[str, float]) -> str:
    """Функция принимает на вход вид и номер карты или счёта с номером"""

    # Преобразуем входное значение в строку, если это число
    if isinstance(types_requisites, float):
        types_requisites = str(types_requisites)

    # Проверка на пустую строку
    if not types_requisites or not types_requisites.strip():
        return "Ошибка: входная строка пустая."

    # Создаём переменные-списки для букв и цифр из аргумента.
    card_type = []
    card_number = []

    # Перебираем аргумент.
    for char in types_requisites:
        # Проверяем, если есть буквы и пробел, то записываем в переменную "card_type" и переводим в нижний регистр.
        if char.isalpha() or char.isspace():
            card_type.append(char.lower())
        # Проверяем, если есть цифры, то записываем в переменную "card_number"
        elif char.isdigit():
            card_number.append(char)
        # Проверяем, если кроме букв и цифр есть другие символы, возвращает ошибку.
        else:
            return "Ошибка: присутствуют другие символы."

    card_number_str = "".join(card_number)
    card_type_str = "".join(card_type).strip()

    # Проверяем, если указан тип карты или счета без номера, возвращает ошибку.
    if len(card_number_str) == 0:
        return f"Ошибка: тип '{card_type_str}' указан без номера."

    # Проверяем длину номера карты или счета
    if len(card_number_str) < 10 or len(card_number_str) > 20:  # Примерные границы для карт и счетов
        return "Ошибка: номер должен содержать от 10 до 20 цифр."

    # Проверяем, если не указан тип карты, возвращает ошибку.
    valid_card_types = ["visa", "счёт", "счет", "мир", "maestro", "mastercard", "union", "american express"]
    if not any(card_type in card_type_str for card_type in valid_card_types):
        return "Ошибка: номер указан без типа карты/счёта."

    # Сверяем, есть ли слова "счет" или "счёт" в строке "card_type_str".
    if "счет" in card_type_str or "счёт" in card_type_str:
        card_type_str = card_type_str.capitalize()
        return f"{card_type_str} **{card_number_str[-4:]}"

    # Проверяем, если тип карты - MasterCard, возвращаем его без изменений
    if "mastercard" in card_type_str:
        return f"MasterCard {card_number_str[:4]} {card_number_str[4:6]} ** **** {card_number_str[-4:]}"

    # Форматирование для остальных карт.
    card_type_str = " ".join(word.capitalize() for word in card_type_str.split())
    masked_card_number = f"{card_type_str} {card_number_str[:4]} {card_number_str[4:6]} ** **** {card_number_str[-4:]}"
    return masked_card_number


@log("mylog.txt")
def get_date(data_full: Union[str]) -> str:
    """Функция, которая принимает на вход строку с датой в формате "YYYY-MM-DDTHH:MM:SS" и
    возвращает дату в формате "ДД.ММ.ГГГГ".
    :rtype: Str
    """

    if not data_full:
        return "Ошибка: входная строка пустая."

    # Проверка на наличие символа "T"
    if "T" not in data_full:
        return "Ошибка: неверный формат даты."

    # Проверка на наличие недопустимых символов в строке
    valid_chars = set("0123456789-:TZ.")
    if not all(c in valid_chars for c in data_full):
        return "Ошибка: дата содержит недопустимые символы."

    # Разделяем дату и время
    date_part = data_full.split("T")[0]

    # Проверка на наличие недопустимых символов в дате
    if not all(c.isdigit() or c == "-" for c in date_part):
        return "Ошибка: дата содержит недопустимые символы."

    date_list = date_part.split("-")

    if len(date_list) != 3:
        return "Ошибка: неверный формат даты."

    year, month, day = date_list

    # Проверка, что все части даты являются цифрами
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return "Ошибка: дата содержит недопустимые символы."

    # Преобразование строковых значений в целые числа для проверки
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)

    # Проверка корректности месяца и дня
    if month_int < 1 or month_int > 12:
        return "Ошибка: некорректный месяц."

    # Проверка количества дней в месяце
    if day_int < 1 or day_int > 31:
        return "Ошибка: некорректный день."

    # Проверка для февраля и месяцев с 30 днями
    if month_int in [4, 6, 9, 11] and day_int > 30:
        return "Ошибка: некорректный день."

    if month_int == 2:
        if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
            if day_int > 29:
                return "Ошибка: некорректный день."
        else:
            if day_int > 28:
                return "Ошибка: некорректный день."

    # Дополнение нулями для дня и месяца
    day = f"{day_int:02}"
    month = f"{month_int:02}"

    # Возвращает строку с датой в формате ДД.ММ.ГГГГ
    return f"{day}.{month}.{year}"


# def get_date(data_full: Union[str]) -> str | ValueError | Any:
#     """Функция, которая принимает на вход строку с датой в формате "YYYY-MM-DDTHH:MM:SS" и
#     возвращает дату в формате "ДД.ММ.ГГГГ".
#     :rtype:"""
#
#     if not data_full:
#         return "Ошибка: входная строка пустая."
#
#     # Проверка на наличие символа "T"
#     if "T" not in data_full:
#         return "Ошибка: неверный формат даты."
#
#     # Проверка на наличие недопустимых символов в полной строке
#     if not all(c.isdigit() or c in ["-", "T", ":", "X", "Z"] for c in data_full):
#         return "Ошибка: дата содержит недопустимые символы."
#
#     # Разделяем дату и время
#     date_part = data_full.split("T")[0]
#
#     # # это для необходимости ввести время в код
#     # time_part = data_full.split("T")[1] if len(data_full.split("T")) > 1 else ""
#
#     # Проверка на наличие недопустимых символов в дате
#     if not all(c.isdigit() or c == "-" for c in date_part):
#         return "Ошибка: дата содержит недопустимые символы."
#
#     date_list = date_part.split("-")
#
#     if len(date_list) != 3:
#         return "Ошибка: неверный формат даты."
#
#     year, month, day = date_list
#
#     # Проверка, что все части даты являются цифрами
#     if not (year.isdigit() and month.isdigit() and day.isdigit()):
#         return "Ошибка: дата содержит недопустимые символы."
#
#     # Преобразование строковых значений в целые числа для проверки
#     year_int = int(year)
#     month_int = int(month)
#     day_int = int(day)
#
#     # Проверка корректности месяца и дня
#     if month_int < 1 or month_int > 12:
#         return "Ошибка: некорректный месяц."
#
#     # Проверка количества дней в месяце
#     if day_int < 1 or day_int > 31:
#         return "Ошибка: некорректный день."
#
#     # Проверка для февраля и месяцев с 30 днями
#     if month_int in [4, 6, 9, 11] and day_int > 30:
#         return "Ошибка: некорректный день."
#
#     if month_int == 2:
#         if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
#             if day_int > 29:
#                 return "Ошибка: некорректный день."
#         else:
#             if day_int > 28:
#                 return "Ошибка: некорректный день."
#
#     # Дополнение нулями для дня и месяца
#     day = "0" + day if len(day) == 1 else day
#     month = "0" + month if len(month) == 1 else month
#
#     # Возвращает строку с датой в формате ДД.ММ.ГГГГ
#     return f"{day}.{month}.{year}"
