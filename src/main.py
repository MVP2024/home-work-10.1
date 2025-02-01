import os

from src.bank_operations import count_operations_by_category, filter_bank_operations
from src.financial_transactions import read_financial_operations_from_csv, read_financial_operations_from_excel
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    lst_transactions = []
    while True:
        choice = input("Пожалуйста, выберите 1, 2 или 3 для выбора из пункта меню: ")
        if choice == "1":
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
            lst_transactions = load_transactions(file_path)
            print("Для обработки выбран JSON-файл.")
            break
        elif choice == "2":
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
            lst_transactions = read_financial_operations_from_csv(file_path)
            print("Для обработки выбран CSV-файл.")
            break
        elif choice == "3":
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
            lst_transactions = read_financial_operations_from_excel(file_path)
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

    # print(f'Загружен список: {lst_transactions}')

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = ''
    while status.upper() not in valid_statuses:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию."
                       "Доступные для фильтровки статусы: (EXECUTED, CANCELED, PENDING): ").upper()
        if status not in valid_statuses:
            print(f"Статус операции \"{status}\" недоступен. Попробуйте снова.")

    # Фильтруем транзакции
    filtered_transactions = filter_by_state(lst_transactions, status)

    # print(f'Вывод списка отфильтрованного по статусу: {status} {filtered_transactions}')
    print(f"Операции отфильтрованы по статусу \"{status.upper()}\".")

    # Запрос на сортировку
    while True:
        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice in ['да', 'нет']:
            break
        print("Неверный ввод. Пожалуйста, введите 'Да' или 'Нет'.")

    if sort_choice == 'да':
        while True:
            order_choice = input("Введите 1 для сортировки по возрастанию или 2 по убыванию: ").strip()
            if order_choice in ['1', '2']:
                break
            print("Неверный ввод. Пожалуйста, введите 1 или 2.")

        ascending = order_choice == '1'
        filtered_transactions = sort_by_date(filtered_transactions, reverse=not ascending)

    # Запрос на фильтрацию по валюте
    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_filter == 'да':
        filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))

    # Запрос на фильтрацию по описанию
    while True:
        description_filter = input(
            "Отфильтровать список транзакций  по описании категорий? Да/Нет: ").strip().lower()
        if description_filter in ['да', 'нет']:
            break
        else:
            print("Неверно. Введите 'да' или 'нет'.")

    if description_filter == 'да':
        # Вводим слово или часть слова по которому будем фильтровать список.
        keyword = input("Введите слово или часть слова для фильтрации по : ").strip()
        filtered_transactions = filter_bank_operations(filtered_transactions, keyword)

    if not filtered_transactions:
        print(f"Не найдено ни одной транзакции, соответствующей критериям фильтрации по описанию: \\{keyword}\\.")

    if filtered_transactions:
        # Переводим в список и возвращаем описание каждой операции после фильтрации списка
        categories = list(transaction_descriptions(filtered_transactions))

        # Подсчитываем количество операций в отфильтрованном списке.
        print(f"Всего банковских операций в выборке: "
              f"{count_operations_by_category(filtered_transactions, categories)}")

        for txn in filtered_transactions:
            # Получаем дату
            print(f"{get_date(txn.get('date'))}: {txn.get('description')}")
            # Получаем маскированные карты или счета
            print(f"{mask_account_card(txn.get('from'))} -> {mask_account_card(txn.get('to'))}")
            # Получаем сумму
            amount = txn.get('amount') or txn.get('operationAmount', {}).get('amount')
            # Получаем валюту
            currency = txn.get('operationAmount', {}).get("currency", {}).get('code') or txn.get('currency_code')
            print(f"Сумма: {int(amount)} {currency}\n")


if __name__ == "__main__":
    main()
