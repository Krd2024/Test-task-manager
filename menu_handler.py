import datetime

from check import get_valid_input, is_digit
from task_manager import TaskManager
from dict_for_compare import (
    get_search_and_count_methods,
    checking_month,
    get_category,
    get_priority,
)

task_manager = TaskManager()


def create_task_handler(update: bool = False):
    """
     Обрабатывает создание или обновление задачи.

    Метод запрашивает у пользователя данные для новой задачи или обновления существующей.
    Пользователю предлагается ввести название задачи, описание, категорию, и другие параметры.
    Также предусмотрена проверка корректности вводимых данных.

    Аргументы:
    update (bool): Флаг, указывающий на то, что задача обновляется. По умолчанию False.
    mock_category: Имитирует ввод категории для тестирования (опционально).
    mock_priority: Имитирует ввод приоритета для тестирования (опционально).
    mock_month: Имитирует ввод месяца для тестирования (опционально).
    task_manager: Экземпляр менеджера задач для взаимодействия с задачами.

    """

    while True:

        # Функция get_valid_input проверяет, что введенное значение не является пустым.
        # Если введена пустая строка (с учётом пробелов), то выводится сообщение об ошибке.
        name = get_valid_input(
            "Введите название книги: ",
            lambda x: len(x.strip()) > 0,
            f"{'-' * 40}\nОШИБКА! Поле 'name' не может быть пустым\n{'-' * 40}",
        )
        break

    while True:

        # Функция get_valid_input проверяет, что введенное значение не является пустым.
        # Если введена пустая строка (с учётом пробелов), то выводится сообщение об ошибке.
        description = get_valid_input(
            "Введите название книги: ",
            lambda x: len(x.strip()) > 0,
            f"{'-' * 40}\nОШИБКА! Поле 'name' не может быть пустым\n{'-' * 40}",
        )
        break
    while True:
        # Выбирать категорию для задачи
        # print("Выберите категорию:\n1 - Работа\n2 - Личное\n3 - Обучение ")
        print("Выберите категорию:")
        for key, val in get_category().items():
            print(f"{key}. {val}")
        category = input("Выбор: ")
        # Проверить корректность ввода категории
        # if category not in ("1", "2", "3"):
        if category not in get_category():
            print(f"{'-' * 40}\nОШИБКА! Категория не определена\n{'-' * 40}")
            continue
        break

    # Получает название категории по ключу
    # Ключ-это номер категории, значение-название категории
    category = get_category(category)

    print("\nСрок выполнения задачи:\n")
    while True:
        # Запрашивает ввод года у пользователя, удаляет все пробелы
        year = input("Введите год: ").replace(" ", "")
        # Проверить, что в строке только числа
        is_digit(year)
        # Если год является числом, то проверяется, что он не меньше 2024
        if is_digit(year):
            # Получить текущий год
            current_year = datetime.datetime.now().year
            # Если год меньше текущего, выводится сообщение об ошибке
            if int(year) < current_year:
                print(f"{'-' * 40}\nОШИБКА! Ушли те времена\n{'-' * 40}")
                continue
        else:
            print(
                f"{'-' * 40}\nОШИБКА! Нужно вводить цифры.Попробуйте ещё раз\n{'-' * 40}"
            )
            continue
        break

    while True:
        # Получить месяц
        month = input("Введите месяц: ").replace(" ", "")
        # Проверить, что в строке только числа
        if is_digit(month):
            # Проверяет, что месяц находится в допустимом диапазоне от 1 до 12
            if int(month) < 1 or int(month) > 12:
                print(
                    f"{'-' * 40}\nnОШИБКА! Этот месяц не отсюда. Попробуйте ещё раз.\n{'-' * 40}"
                )
                continue
        else:
            print(f"{'-' * 40}\nОШИБКА! Так не пойдёт, нужны цифры\n{'-' * 40}")
            continue
        break
    while True:
        # Полумить день
        day = input("Введите день: ").replace(" ", "")
        # Проверить, что в строке только числа
        if is_digit(day):

            # Вызывает функцию "checking_month" проверки соответствия кол-ва дней в месяце
            # В функции предусмотрина проверка на високостность
            # Получат True или False
            if not checking_month(month, int(day), int(year)):
                print(
                    f"{'-' * 40}\nnОШИБКА! Эти дни нам не знакомы.Попробуйте ещё раз\n{'-' * 40}"
                )
                continue
        else:
            print(f"{'-' * 40}\nnОШИБКА! Непонятно, что за день\n{'-' * 40}")
            continue
        break
    # Собрать в одну переменную дату в формате 2024-12-3
    period_execution = f"{year}-{month}-{day}"

    while True:
        # Выбрать приоритет для задачи
        print("Выберите приоритет задачи: ")

        # Перечисляет возможные приоритеты
        # Берёт их из модуля со словарём
        for key, val in get_priority().items():
            print(f"{key}. {val}")

        # Выбор пользователя
        priority = input("\nВыбор: ").replace(" ", "")

        # Проверка ввода на соответствие предложенным вариантам
        if priority not in get_priority():
            print(f"{'-' * 40}\nОШИБКА! Приоритет не определён\n{'-' * 40}")
            continue
        break
    # Получает значение (приоритет) из словаря
    # согластно выбранному варианту
    priority = get_priority(priority)

    # При редактировании задачи
    # возвращает отредактированные поля

    if update:
        return (
            name,
            description,
            category,
            period_execution,
            priority,
        )
    # При создании новой задачи вызыват метод
    # добавления задачи в список
    task_manager.add_task(
        name,
        description,
        category,
        period_execution,
        priority,
    )


def delete_task_handler():
    """
    Функция вызывается из меню при
    выборе пункта: "удаление"
    Запрашивае ID задачи для удаления,проверяет
    состоит ли ввод для id задачи только из цифр
    Если id является числом, вызвать метод удаления задачи
    """

    while True:
        # ID задачи получить
        book_id = input("Введите ID задачи для удаления: ").replace(" ", "")

        # Функция is_digit(book_id) проверяет, состоит ли ввод для id задачи только из цифр.
        if not is_digit(book_id):
            print(f"{'-' * 40}\nОШИБКА! Только числа\n{'-' * 40}")
            continue
        # Вызвает метод удаления задачи
        task_manager.delete_task(int(book_id))
        break


def search_task_hendler(mock_keywords=None):
    """
    Выводит список доступных методов поиска, определённых в 'get_search_and_count_methods()'.
    Принимает выбор пользователя.
    Проверяет корректность выбора:
        - Если выбор некорректен, выводит сообщение об ошибке и повторяет запрос.
        - Если выбор корректен, выполняет соответствующий метод поиска.

    """

    while True:
        print("ВЫБЕРИТЕ ПАРАМЕТРЫ ПОИСКА:")

        # Предлагает возможные метода поиска из словаря
        for key, value in get_search_and_count_methods().items():
            print(f"{key}. {value['label']}")

        choice_search = input("\nВыбор: ").replace(" ", "")
        # Проверяет выбор пользовате на соответствие методам поиска
        if choice_search not in get_search_and_count_methods():
            print(f"{'-' * 40}\nОШИБКА! параметры поиска не определены\n{'-' * 40}")
            continue

        # "1": {"label": "По ключевым словам", "action": search_keywords},
        # "2": {"label": "По статусу выполнения", "action": search_status},
        # В зависимости от выбора пользователя запускает одину из функций:
        # - поиск по ключевым словам
        # - поиск по статусу выполнения
        get_search_and_count_methods()[choice_search]["action"]()

        break


def display_all_task_hendler():
    task_manager.display_all_task()


def display_categories_hendler():
    while True:
        # получить символический номер категории
        print("Выберите категорию:\n1 - Работа\n2 - Личное\n3 - Обучение ")
        num_category = input("\nВыбор: ").replace(" ", "")

        # Если категория не в рамках предложенного, вывести ошибку.
        # Если категория в рамках предложенного,вызвать метод вывода
        # задач выбранной категории
        if num_category not in ("1", "2", "3"):
            # print("-" * 40)
            print(f"{'-' * 40}\nОШИБКА! Категория не определена\n{'-' * 40}")

            continue
        break

    # Получает название категории по ключу
    # Ключ-это номер категории, значение-название категории
    category = get_category(num_category)

    # Вызывает метод показа задач в выбранной категории
    task_manager.search(category=category)


def update_task_handler(update_status: bool = False) -> None:
    """
    Обработчик обновления задачи или её статуса.

    - Если параметр 'update_status' равен True, обновляет статус задачи по ID.
    - Если параметр 'update_status' равен False, обновляет данные задачи по ID.
    """
    # Получает список всех задач
    tasks = task_manager.get_tasks()

    while True:
        # Отображает доступные задачи для выбора
        print(f"{'-' * 40}\nВЫБЕРИТЕ ID ЗАДАЧИ ИЗ СПИСКА:\n")
        for task in tasks:
            print(f"{task.name} | ID:{task.id} | {task.status}")
        # Запрашивает ID задачи
        task_id = input("Введите ID: ").replace(" ", "")
        # Проверяет, является ли введённый ID числом
        if is_digit(task_id):
            if update_status:
                # Обновляет только статус задачи, если флаг `update_status` True
                task_manager.update_status(int(task_id))
                break
            # Обновляет данные задачи
            task_manager.update_task(int(task_id))
            break
        print(f"{'-' * 40}\nОШИБКА! Здесь нет таких ID{'-' * 40}\n")
        continue
