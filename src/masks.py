from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:


    """Функция принимает на вход номер карты и

       возвращает замаскированный номер

    в формате XXXX XX** **** XXXX
    """

    masked_number = card_number[:4] + " " + card_number[6:8] + "** **** " + card_number[-4:]
    return masked_number


def get_mask_account(account_number: Union[str]) -> Union[str]:

    """
    Функция принимает на вход номер счёта и

    возвращает замаскированный счёт в формате

                **XXXX
    """
    masked_number = "**" + account_number[-4:]
    return masked_number
