def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    return [dictionary for dictionary in list_dictionary if dictionary.get("state", "non") == state]


list_d = [
    {"id": 939719570, "state": "EXECUTED", "date": "2023-06-30Т02: 08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "RR", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064591, "state": 1234, "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064591, "state": "CANCELED", "date": "2012-10-14Т08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]


def sort_by_date(list_dictionary: list, sort_order: bool = True) -> list:
    sort_date = sorted(list_dictionary, key=lambda x: x["date"], reverse=sort_order)
    return sort_date


print(sort_by_date(list_d, sort_order=True))
