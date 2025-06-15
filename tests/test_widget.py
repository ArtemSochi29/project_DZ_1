import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    ("number", "new_string"),
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ],
)
def test_mask_account_card(number, new_string):
    assert mask_account_card(number) == new_string


@pytest.mark.parametrize(("date", "new_date"), [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(date, new_date):
    assert get_date(date) == new_date
