def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    list_executed: list = []
    list_canceled: list = []
    list_different: list = []
    for item in list_dictionary:
        if item.get("state") == state:
            list_executed.append(item)
            list_canceled.append(item)
            list_different.append(item)
    if state == "EXECUTED":
        return list_executed
    elif state == "CANCELLED":
        return list_canceled
    else:
        return list_different


list_d = [
    {"id": 939719570, "state": "EXECUTED", "date": "2023-06-30Т02: 08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "RR", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064591, "state": 1234, "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064591, "state": "CANCELED", "date": "2012-10-14Т08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

# def filter_by_state(
#     inform_dict: list[dict[str, Any]], state_id: str = "EXECUTED"
# ) -> list[dict[str, Any]]:
#     """Функция, которая принимает на вход список словарей и
#     значений для ключа state и выдает новый список с заданным ключом"""
#     new_list_state = []
#     try:
#         for i in inform_dict:
#             if i.get("state") == state_id:
#                 new_list_state.append(i)
#         return new_list_state
#     except (AttributeError, TypeError):
#         print("AttributeError", "TypeError")
#     except Exception as e:
#         print(e)
#
#
# def sort_by_date(
#     inform_dict: list[dict[str, Any]], reverse: bool = True
# ) -> list[dict[str, Any]]:
#     """Функция сортировки по дате"""
#     sorted_inform_state = sorted(inform_dict, key=lambda x: x["date"], reverse=reverse)
#     return sorted_inform_state

def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    list_executed: list = []
    list_canceled: list = []
    list_different: list = []
    for item in list_dictionary:
        if item.get("state") == state:
            list_executed.append(item)
            list_canceled.append(item)
            list_different.append(item)
    if state == "EXECUTED":
        return list_executed
    elif state == "CANCELLED":
        return list_canceled
    else:
        return list_different
list_d = [{"id": 939719570, "state": "EXECUTED", "date": "2023-06-30Т02: 08:58.425572"},
          {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
          {"id": 615064591, "state": "RR", "date": "2018-10-14T08:21:33.419441"},
          {"id": 615064591, "state": 1234, "date": "2018-10-14T08:21:33.419441"},
          {"id": 615064591, "state": "CANCELED", "date": "2012-10-14Т08:21:33.419441"},
          {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]

def sort_by_date(list_dictionary: list, sort_order: bool = True) -> list:
    sort_date = sorted(list_dictionary, key=lambda x: x["date"], reverse=sort_order)
    return sort_date


print(sort_by_date(list_d, sort_order=True))
