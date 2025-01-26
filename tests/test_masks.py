import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def test_card_num():
    return ['Visa Super Puper 123456789012345612',
            'Visa Super 1234567890123456',
            'Visa 1234567890123456121']

@pytest.mark.parametrize('card_num, expected', [('123456789012345612', '1234 56** **** 5612'),
                                                ('1234567890123456','1234 56** **** 3456'),
                                                ('1234567890123456121', '1234 56** **** 6121')])
def test_get_mask_card_number (card_num, expected):
    assert get_mask_card_number (card_num) == expected


# def test_get_mask_card_number (card_num: Union[str]) -> Union[str]:
#     "Функция возвращает замаскированный номер карты"
#     if len(card_num) == 20:
#         return f"**{card_num[-4:]}"
#     else:
#         return "Данные не верны"
#
# def test_get_mask_account(accounts_num: Union[str]) -> Union[str]:
#     "Функция возвращает замаскированные номера счета"
#     if accounts_num:
#         return f"{accounts_num[:4]}" " " f"{accounts_num[4:6]}** ***" " " f"{accounts_num[-4:]}"
#     else:
#         return "Данные не верны"