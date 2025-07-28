from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Маскирует информацию о картах и счетах"""
    user_input_str = str(user_input)
    if "Счет" in user_input_str:
        return f"Счет {get_mask_account(user_input_str)}"
    else:
        card_numbers = get_mask_card_number(user_input_str[-16:])
        card_mask = user_input_str.replace(user_input_str[-16:], card_numbers)
        return card_mask


def get_date(date: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
