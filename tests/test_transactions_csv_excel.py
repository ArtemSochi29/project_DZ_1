from unittest.mock import patch

import pytest
from pandas import DataFrame

from src.transactions_csv_excel import transactions_csv_read, transactions_excel_read


def test_transactions_csv_read():
    return_v = [
        {
            "id": 4699552.0,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        }
    ]
    with patch("pandas.read_csv", return_value=DataFrame(return_v)):
        data = transactions_csv_read("")
        assert data == return_v
    with pytest.raises(FileNotFoundError):
        transactions_csv_read("")


def test_transactions_excel():
    return_v = [
        {
            "id": 4699552.0,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        }
    ]
    with patch("pandas.read_excel", return_value=DataFrame(return_v)):
        data = transactions_excel_read("")
        assert data == return_v
    with pytest.raises(FileNotFoundError):
        transactions_excel_read("")
