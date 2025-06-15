from typing import Any, Dict, Generator, Iterable


def filter_by_currency(
    transactions: Iterable[Dict[str, Any]], currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """Фильтрует список транзакций, по указанной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterable[str]:
    for transaction in transactions:
        yield transaction.get("description", "Перевод организации")


def transaction_next_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterable[str]:
    for transaction in transactions:
        yield transaction.get("description", "Перевод организации")


def card_number_generator(start: int, stop: int) -> list:
    for num in range(start, stop + 1):
        card_number = str(num)
        while len(card_number) < 16:
            card_number = "0" + card_number

        if 1 > int(card_number) or int(card_number) > 9999999999999999:
            raise ValueError("Недопустимый номер карты")

        form_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        if 1 <= int(card_number) <= 9999999999999999:
            yield form_card_number
