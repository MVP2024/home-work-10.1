from typing import Union


def mask_account_card(types_requisites: Union[str]) -> str:
    """Функция принимает на вход вид и номер карты или счёт с номером"""

    if "Счёт" in types_requisites or "Счет" in types_requisites:

        """если указан счёт, возвращает <type> <**XXXX>"""

        return types_requisites[:4] + " " + "**" + types_requisites[-4:]

    elif "Visa" in types_requisites or "MasterCard" in types_requisites or "Maestro" in types_requisites:

        """возвращает название и замаскированный номер, если указана карта

        в формате < type > < XXXX XX ** ** ** XXXX >"""

        return types_requisites[0:-12] + " " + "** **** " + types_requisites[-4:]


def get_date(data_full: Union[str]) -> str:
    """Функция, которая принимает на вход строку с датой в формате

    "2024-03-11T02:26:18.671407"

    и возвращает строку с датой в формате

    'ДД.ММ.ГГГГ'."""

    year = data_full[:4]
    month = data_full[5:7]
    day = data_full[8:10]

    return f"{year}.{month}.{day}"
