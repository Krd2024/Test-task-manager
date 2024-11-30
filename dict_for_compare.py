def get_category(num: str) -> str:
    dict_category = {"1": "Работа", "2": "Личное", "3": "Обучение"}
    return dict_category[num]


def get_status(num: str) -> str:
    dict_status = {"1": "Выполнена", "2": "Не выполнена"}
    return dict_status[num]


def get_priority(num: str) -> str:
    dict_priority = {"1": "Низкий", "2": "Средний", "3": "Высокий"}
    return dict_priority[num]


def checking_month(month, day, year):

    dict_days_in_month = {
        "1": 31,
        "2": 29,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 31,
        "9": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        dict_days_in_month["2"] = 28

    # print(list(range(1, dict_days_in_month[month] + 1)))
    return day in list(range(1, dict_days_in_month[month] + 1))


# print(checking_month("1", 40))
# year = 2024
# print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
# print(checking_month("2", 29, 2023))
