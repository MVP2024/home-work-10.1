from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

''' Вывод всех функций. '''
if __name__ == "__main__":

    """Вывод замаскированного номера карты и счёта"""
    print(get_mask_card_number('7854121223455678'))
    print(get_mask_account('7854121223455678'))


    """ Вывод название карты и скрытого номера
        или счёта со скрытым номером """
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(mask_account_card('Счет 73654108430135874305'))

    """Вывод даты"""
    print(get_date("2024-03-11T02:26:18.671407"))


Пример использования.
list_of_dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


print(filter_by_state(list_of_dictionaries))
print(sort_by_date(data, True))
