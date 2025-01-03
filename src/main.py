from src.data import data, transactions
from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

""" Вывод всех функций. """
if __name__ == "__main__":
    """Вывод замаскированного номера карты и счёта"""
print(get_mask_card_number("7854121223455678"))
print(get_mask_card_number("78541212234"))
print(get_mask_card_number("7854121223455678444445"))
print(get_mask_card_number("78541апр555678рп"))
print(get_mask_card_number(""))
print(get_mask_account("7854121223455678"))
print(get_mask_account("78541211-*/45567"))
print(get_mask_account(""))

""" Вывод название карты и скрытого номера
 или счёта со скрытым номером """
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Visa Silver 7000792289606361"))
print(mask_account_card(""))
print(mask_account_card("Maestro Bobr Kurwa 2345567889455565"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Счёт 7365410/**874305"))
print(mask_account_card("Счёт 2345234578894556"))
print(mask_account_card("123456"))
print(mask_account_card("MasterCard 123456"))
print(mask_account_card("MasterCard 1234567890369854"))
print(mask_account_card("MasterCard 12345656756767657676"))
print(mask_account_card("MasterCard 123/*/*///*//*kjhkjhkjhkj456"))
print(mask_account_card("MasterCard 123456/*/*/"))

"""Вывод даты"""
print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2054---3--11:26:18.671407"))
print(get_date(""))
print(get_date("4587^1"))

"""Вывод отсортированного списка по state"""
print(filter_by_state(data, "EXECUTED"))
print(filter_by_state(data, "CANCELED"))

"""Вывод списка по date отсортированного (по-умолчанию) на убывание"""
print(sort_by_date(data, True))

"""Вызов функции filter_by_currency"""
usd_transactions = filter_by_currency(transactions, "USD")
"""Вывод отфильтрованных транзакций"""
for transaction in usd_transactions:
    print(transaction)
