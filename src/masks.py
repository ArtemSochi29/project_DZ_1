from typing import Union


def get_mask_card_number(card_num: Union[str, int]) -> str:
    """Возвращает маску номера по правилу XXXX XX ** **** XXXX"""

    mask_card_num = str(card_num)
    mask_card_num = mask_card_num[:4] + " " + mask_card_num[4:6] + "** **** " + mask_card_num[-4:]

    return mask_card_num


def get_mask_account(account: Union[str, int]) -> str:
    """Возвращает маску номера по правилу **XXXX"""

    mask_account = str(account)
    mask_account = "**" + mask_account[-4:]

    return mask_account
