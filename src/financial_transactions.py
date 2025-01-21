import csv
from typing import Dict

from src.main import transaction


def read_financial_operations_from_csv(file_path: str) -> list[Dict[str, str]]:
	"""
	Считывает финансовые операции из файла csv
	:param file_path:
	:return: Список словарей с транзакциями.
	"""

	transactions_from_csv = []
	with open(file_path, 'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			transaction.append(row)
	return transactions_from_csv

