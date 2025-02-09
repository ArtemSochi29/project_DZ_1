import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, currency",
    [
        (
            [
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
            ],
            "USD",
        )
    ],
)
def test_filter_by_currency(transactions, currency):
    filtered_transactions = filter_by_currency(transactions, currency)
    assert next(filtered_transactions)["id"] == 939719570
    assert next(filtered_transactions)["id"] == 142264268
    assert next(filtered_transactions)["id"] == 142264269
    assert next(filtered_transactions)["id"] == 142264270
    assert next(filtered_transactions)["id"] == 142264271


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {"}description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Оплата"},
                {"description": "Оплата не прошла"},
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Оплата",
                "Оплата не прошла",
            ],
        ),
    ],
)
def test_transaction_descriptions(transactions, expected):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected


# Параметризация теста
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (4000, 4002, ["4000 4000 4000 4000", "4001 4001 4001 4001"]),
        (5000, 5001, ["5000 5000 5000 5000"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator())
    assert result == expected
