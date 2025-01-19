from typing import Any


def filter_by_state(
    inform_dict: list[dict[str, Any]], state_id: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Функция, которая принимает на вход список словарей и
    значений для ключа state и выдает новый список с заданным ключом"""
    new_list_state = []
    try:
        for i in inform_dict:
            if i.get("state") == state_id:
                new_list_state.append(i)
        return new_list_state
    except (AttributeError, TypeError):
        print("AttributeError", "TypeError")
    except Exception as e:
        print(e)


def sort_by_date(
    inform_dict: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """Функция сортировки по дате"""
    sorted_inform_state = sorted(inform_dict, key=lambda x: x["date"], reverse=reverse)
    return sorted_inform_state