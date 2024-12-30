from typing import List, Dict, Any, Iterator
def filter_by_currency(transactions: list[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    for transaction in transactions:
        if transaction.get('operationAmount', {})get('currency', {}).get('code') == currency:
            yield transaction


