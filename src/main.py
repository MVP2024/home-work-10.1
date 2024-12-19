from src.data import data
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

""" Вывод всех функций. """
if __name__ == "__main__":

    """Вывод замаскированного номера карты и счёта"""
    print(get_mask_card_number("7854121223455678"))
    print(get_mask_account("7854121223455678"))

    """ Вывод название карты и скрытого номера
        или счёта со скрытым номером """
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

    """Вывод даты"""
    print(get_date("2024-03-11T02:26:18.671407"))

    """Вывод отсортированного списка по state"""
    print(filter_by_state(data, "EXECUTED"))
    print(filter_by_state(data, "CANCELED"))

    """Вывод отсортированного списка по date"""
    print(sort_by_date(data, True))
    print(sort_by_date(data, False))
