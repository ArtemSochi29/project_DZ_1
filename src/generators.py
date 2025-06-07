from typing import Dict, Any, Generator, Iterable


def filter_by_currency(
    transactions: Iterable[Dict[str, Any]], currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """Фильтрует список транзакций, по указанной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264269,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264270,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 19708645243227258555",
        "to": "Счет 75651667383060284166",
    },
    {
        "id": 142264271,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 19708645243227258577",
        "to": "Счет 75651667383060284188",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(5):
    print(next(usd_transactions))


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterable[str]:
    for transaction in transactions:
        yield transaction.get("description", "Перевод организации")


def transaction_next_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterable[str]:
    for transaction in transactions:
        yield transaction.get("description", "Перевод организации")


descriptions = transaction_descriptions(transactions)
for i in range(5):
    print((next(descriptions)))


def card_number_generator(start, stop):
    for num in range(start, stop + 1):
        card_number = str(num)
        while len(card_number) < 16:
            card_number = '0' + card_number

        if 1 > int(card_number) or int(card_number) > 9999999999999999:
            raise ValueError("недопустимый номер карты")

        form_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        if 1 <= int(card_number) <= 9999999999999999:
            yield form_card_number
