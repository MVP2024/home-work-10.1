# import os
# import unittest
# from unittest.mock import patch, MagicMock
#
# from src.logger import setup_logger
# from src.main import main
# from src.bank_operations import count_operations_by_category, filter_bank_operations
# from src.financial_transactions import read_financial_operations_from_csv, read_financial_operations_from_excel
# from src.generators import filter_by_currency, transaction_descriptions
# from src.processing import filter_by_state, sort_by_date
# from src.utils import load_transactions
# from src.widget import get_date, mask_account_card
# import unittest
# from unittest.mock import patch
# from src.main import main
#
# class TestMainFunction(unittest.TestCase):
#
#     @patch('builtins.print')  # Мокаем print
#     @patch('builtins.input', side_effect=['4'])  # Неверный ввод
#     def test_invalid_menu_choice(self, mocked_input, mock_print):
#         main()
#         mock_print.assert_any_call("Неверный выбор. Завершение программы.")
#         print("Все вызовы mock_print в test_invalid_menu_choice:", mock_print.call_args_list)
#
#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['2'])  # Выбор CSV
#     @patch('src.financial_transactions.read_financial_operations_from_csv',
#            return_value=[{"date": "2023-01-01", "description": "Тестовая транзакция", "amount": 1000}])
#     def test_load_csv(self, mock_read_csv, mock_input, mock_print):
#         main()
#         mock_read_csv.assert_called_once()
#         mock_print.assert_any_call("Для обработки выбран CSV-файл.")
#         print("Все вызовы mock_print в test_load_csv:", mock_print.call_args_list)
#
#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['4'])  # Неверный выбор
#     def test_invalid_choice(self, mock_input, mock_print):
#         main()
#         mock_print.assert_any_call("Неверный выбор. Завершение программы.")
#         print("Все вызовы mock_print в test_invalid_choice:", mock_print.call_args_list)
#
#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['1', 'INVALID_STATUS'])  # Неверный статус
#     @patch('src.utils.load_transactions',
#            return_value=[{"date": "2023-01-01", "description": "Тестовая транзакция", "amount": 1000}])
#     def test_invalid_status(self, mock_load, mock_input, mock_print):
#         main()
#         mock_print.assert_any_call('Статус операции "INVALID_STATUS" недоступен. Завершение программы.')
#         print("Все вызовы mock_print в test_invalid_status:", mock_print.call_args_list)
#
#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['1', 'EXIT'])  # Выход из программы
#     @patch('src.utils.load_transactions',
#            return_value=[{"date": "2023-01-01", "description": "Тестовая транзакция", "amount": 1000}])
#     def test_exit_choice(self, mock_load, mock_input, mock_print):
#         main()
#         mock_print.assert_any_call("Выход из программы.")
#         print("Все вызовы mock_print в test_exit_choice:", mock_print.call_args_list)
#
# if __name__ == '__main__':
#     unittest.main()
