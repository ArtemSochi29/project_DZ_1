from src import masks, widget


print(masks.get_mask_card_number(7000792289606361))
print(masks.get_mask_account(73654108430135874305))
print(widget.mask_account_card("Visa Platinum 7000792289606361"))
print(widget.mask_account_card("Maestro 7000792289606361"))
print(widget.mask_account_card("Счет 73654108430135874305"))
print(widget.get_date("2024-03-11T02:26:18.671407"))
