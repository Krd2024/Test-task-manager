def get_category_for_menu(num: str) -> str:
    dict_category = {"1": "Работа", "2": "Личное", "3": "Обучение"}
    return dict_category[num]


def get_status_for_search(num: str) -> str:
    dict_status = {"1": "Выполнена", "2": "Не выполнена"}
    return dict_status[num]
