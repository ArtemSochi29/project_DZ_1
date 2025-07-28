import re
from typing import List, Dict


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    print(f"Ищем '{search}' в данных...")
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = [transaction for transaction in data if pattern.search(transaction.get("description"))]
    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Возвращает словарь с количеством операций по категориям."""
    category_count = {category: 0 for category in categories}
    for transaction in data:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    return category_count
