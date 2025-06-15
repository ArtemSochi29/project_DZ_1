import logging

from src.settings import LOGS_DIR

name_file = "masks"
log_file = LOGS_DIR / "masks.log"

masks_logger = logging.getLogger(name_file)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s: %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты"""
    try:
        masks_logger.info(f"Выполняем проверку номера карты {card_number}")
        card_number_without_spaces = card_number.replace(" ", "")
        if len(card_number_without_spaces) != 16:
            masks_logger.error(f"Номер карты введен не корректно {card_number}")
            return "Номер карты введен не корректно"

        card_number_mask = (
            f"{card_number_without_spaces[:4]} {card_number_without_spaces[4:6]}** "
            f"**** {card_number_without_spaces[-4:]}"
        )
        masks_logger.info("Функция работает корректно")
        return card_number_mask
    except Exception as ex:
        masks_logger.error(f"Произошла ошибка {ex}")
        raise Exception(f"Произошла ошибка {ex}")


def get_mask_account(account_number: str) -> str:
    """
    Маскировка номера счета
    :param account_number: Номер счета
    :return: Замаскированный счет (Формат: **xxxx)
    """
    masks_logger.info("Функция начата")
    result = f"**{account_number[-4:]}"
    masks_logger.info("Функция закончена")
    return result


if __name__ == "__main__":
    print(get_mask_card_number("73654108430135874305"))
