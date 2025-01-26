import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import csv
import pandas as pd
from typing import List, Dict
from src.financial_transactions import (EmptyFileError, FileReadError, InvalidFileFormatError,
                                        read_financial_operations_from_csv, read_financial_operations_from_excel)


# Тестирование функции read_financial_operations_from_csv.
class TestReadFinancialOperationsFromCSV(unittest.TestCase):

    @patch("os.path.isfile", return_value=False)  # Мокируем os.path.isfile, чтобы он возвращал False
    def test_file_not_found(self, mock_isfile):
        with self.assertRaises(FileNotFoundError):
            read_financial_operations_from_csv("non_existent_file.csv")

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    def test_invalid_file_format(self, mock_isfile):
        with self.assertRaises(InvalidFileFormatError):
            read_financial_operations_from_csv("invalid_file.txt")

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    @patch("builtins.open", new_callable=mock_open, read_data="")  # Мокируем open, чтобы вернуть пустые данные
    def test_empty_file(self, mock_file, mock_isfile):
        with self.assertRaises(EmptyFileError):
            read_financial_operations_from_csv("empty_file.csv")

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    @patch("builtins.open", new_callable=mock_open,
           read_data="column1,column2\nvalue1,value2\n")  # Мокируем open с данными
    def test_successful_read(self, mock_file, mock_isfile):
        result = read_financial_operations_from_csv("valid_file.csv")
        expected = [{'column1': 'value1', 'column2': 'value2'}]
        self.assertEqual(result, expected)

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    @patch("builtins.open", new_callable=mock_open)  # Мокируем open
    def test_read_file_error(self, mock_file, mock_isfile):
        mock_file.side_effect = IOError("Ошибка чтения файла")  # Настраиваем исключение для mock_file
        with self.assertRaises(FileReadError):
            read_financial_operations_from_csv("error_file.csv")


# Тестирование функции read_financial_operations_from_excel.
class TestReadFinancialOperationsFromExcel(unittest.TestCase):

    @patch("os.path.isfile", return_value=False)  # Мокируем os.path.isfile, чтобы он возвращал False
    def test_file_not_found(self, mock_isfile):
        with self.assertRaises(FileNotFoundError):
            read_financial_operations_from_excel("non_existent_file.xlsx")

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    def test_invalid_file_format(self, mock_isfile):
        with self.assertRaises(InvalidFileFormatError):
            read_financial_operations_from_excel("invalid_file.txt")

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    @patch("pandas.read_excel")  # Мокируем pandas.read_excel
    def test_read_file_error(self, mock_read_excel, mock_isfile):
        # Настраиваем mock, чтобы он вызывал исключение при чтении файла
        mock_read_excel.side_effect = Exception("Ошибка чтения файла")
        with self.assertRaises(FileReadError):
            read_financial_operations_from_excel("error_file.xlsx")

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    @patch("pandas.read_excel")  # Мокируем pandas.read_excel
    def test_empty_file(self, mock_read_excel, mock_isfile):
        # Настраиваем mock, чтобы возвращать пустой DataFrame
        mock_read_excel.return_value = pd.DataFrame()
        with self.assertRaises(EmptyFileError):
            read_financial_operations_from_excel("empty_file.xlsx")

    @patch("os.path.isfile", return_value=True)  # Мокируем os.path.isfile, чтобы он возвращал True
    @patch("pandas.read_excel")  # Мокируем pandas.read_excel
    def test_successful_read(self, mock_read_excel, mock_isfile):
        # Настраиваем mock, чтобы возвращать DataFrame с данными
        mock_read_excel.return_value = pd.DataFrame({
            'column1': ['value1', 'value2'],
            'column2': ['value3', 'value4']
        })
        result = read_financial_operations_from_excel("valid_file.xlsx")
        expected = [
            {'column1': 'value1', 'column2': 'value3'},
            {'column1': 'value2', 'column2': 'value4'}
        ]
        self.assertEqual(result, expected)