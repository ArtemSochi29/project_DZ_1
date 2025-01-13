from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Маскирует информацию о картах и счетах"""
    if "Счет" in user_input:
        return f"Счет {get_mask_account(user_input)}"
    else:
        card_numbers = get_mask_card_number(user_input[-16:])
        card_mask = user_input.replace(user_input[-16:], card_numbers)
        return card_mask


def get_date(date: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"