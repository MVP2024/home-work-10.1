import os
from typing import List

from src.bank_operations import count_operations_by_category, filter_bank_operations
from src.financial_transactions import read_financial_operations_from_csv, read_financial_operations_from_excel
from src.generators import filter_by_currency, transaction_descriptions
from src.logger import setup_logger
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions, logger
from src.widget import get_date, mask_account_card

# Логируем инициализацию модуля
logger.info("Инициализация модуля main")


def main() -> None:
    """Главная функция программы для работы с банковскими транзакциями.

    Настраивает логгер, отображает меню для выбора источника данных и загружает
    транзакции из выбранного файла (JSON, CSV или XLSX). Если транзакции не найдены,
    выводит соответствующее сообщение.
    """
    # Настройка логгера для модуля main
    logger = setup_logger(__name__)

    logger.info("Программа запущена.")
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    lst_transactions = []

    # Выбор пункта меню
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Пожалуйста, введите номер пункта: ")

        if choice == "1":
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
            lst_transactions = load_transactions(file_path)
            logger.info("Обработка JSON-файла: %s", file_path)
            print("Для обработки выбран JSON-файл.")
            break
        elif choice == "2":
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
            lst_transactions = read_financial_operations_from_csv(file_path)
            logger.info("Обработка CSV-файла: %s", file_path)
            print("Для обработки выбран CSV-файл.")
            break
        elif choice == "3":
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
            lst_transactions = read_financial_operations_from_excel(file_path)
            logger.info("Обработка XLSX-файла: %s", file_path)
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            logger.warning("Неверный выбор пользователя: %s", choice)
            print(f'Пункт "{choice}" недоступен. Пожалуйста, попробуйте снова.')

    if not lst_transactions:
        logger.warning("Не найдено ни одной транзакции в файле.")
        print("Не найдено ни одной транзакции в файле.")
        return

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    # Запрос статуса с циклом
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию "
            "(EXECUTED, CANCELED, PENDING) или EXIT для выхода из программы: "
        ).upper()

        if status == "EXIT":
            logger.info("Пользователь вышел из программы.")
            print("Выход из программы.")
            return

        if status in valid_statuses:
            break
        else:
            logger.warning("Некорректный статус операции: %s", status)
            print(f'Статус операции "{status}" недоступен. Пожалуйста, попробуйте снова.')

    # Фильтруем транзакции
    filtered_transactions = filter_by_state(lst_transactions, status)
    logger.info("Фильтрация транзакций по статусу: %s", status)

    # Запрос на сортировку
    while True:
        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice == "да":
            while True:
                order_choice = input(
                    "Введите 1, чтобы отсортировать по возрастанию или 2, чтобы отсортировать по убыванию: "
                ).strip()
                if order_choice in ["1", "2"]:
                    ascending = order_choice == "1"
                    logger.info(f"Сортировка по {'возрастанию' if ascending else 'убыванию'}.")
                    print(f"Сортировка по {'возрастанию' if ascending else 'убыванию'}.")
                    filtered_transactions = sort_by_date(filtered_transactions, reverse=not ascending)
                    break
                else:
                    logger.warning("Неверный ввод для сортировки.")
                    print("Неверный ввод. Пожалуйста, попробуйте еще раз.")
            break
        elif sort_choice == "нет":
            logger.info("Сортировка не требуется.")
            print("Сортировка не требуется.")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 'Да' или 'Нет'.")

    # Запрос на фильтрацию по валюте
    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_filter == "да":
        filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
        logger.info("Фильтрация по валюте: выбраны только рублевые транзакции.")

    # Запрос на фильтрацию по описанию
    description_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    )
    if description_filter == "да":
        keyword = input("Введите слово для фильтрации по описанию: ")
        filtered_transactions = filter_bank_operations(filtered_transactions, keyword)
        logger.info(f"Фильтрация по описанию: выбраны транзакции с ключевым словом '{keyword}'.")

    if filtered_transactions:
        # Переводим в список и возвращаем описание каждой операции после фильтрации списка
        categories: List[str] = list(transaction_descriptions(filtered_transactions))

        # Подсчитываем количество операций в отфильтрованном списке.
        print(
            f"Всего банковских операций в выборке: "
            f"{count_operations_by_category(filtered_transactions, categories)}"
        )

        # Выводим информацию о каждой транзакции
        for txn in filtered_transactions:
            # Получаем дату
            date_str = get_date(txn.get("date"))
            print(f"{date_str}: {txn.get('description')}")

            # Получаем маскированные карты или счета
            print(f"{mask_account_card(txn.get('from'))} -> {mask_account_card(txn.get('to'))}")

            # Получаем сумму и округляем ее до целого числа
            amount = txn.get("amount") or txn.get("operationAmount", {}).get("amount")
            amount = int(float(amount))  # Округление до целого числа

            # Получаем валюту
            currency: str = txn.get("operationAmount", {}).get("currency", {}).get("code") or txn.get("currency_code")
            print(f"Сумма: {amount} {currency}\n")

            # Логируем каждую транзакцию
            logger.info(
                f"Транзакция: Дата - {date_str}, Описание - {txn.get('description')}, " f"Сумма - {amount} {currency}"
            )

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        logger.warning("Не найдено ник какой-либо транзакции после фильтрации.")


if __name__ == "__main__":
    main()
