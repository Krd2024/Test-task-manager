from check import is_digit
from dict_for_compare import checking_month, get_category, get_priority, get_status

from task_manager import TaskManager

# from task_manager_import import get_task_manager


# task_manager = get_task_manager()
task_manager = TaskManager()


def create_task_handler(update: bool = False):
    print(update, "<<<<<<<<<< update")

    # Заголов для задачи
    while True:
        name = input("Введите название: ")
        # Проверить поле на наличие символов
        if len(name.replace(" ", "")) == 0:
            print(f"{'-' * 40}\nОШИБКА! Поле 'name' не может быть пустым\n{'-' * 40}")
            continue
        break
    while True:
        description = input("Введите описание: ")
        # Проверить поле описание на наличие символов
        if len(description.replace(" ", "")) == 0:
            print(f"{'-' * 40}\nПоле 'description' не может быть пустым\n{'-' * 40}")
            continue
        break
    while True:
        # Выбирать категорию для задачи
        print("Выберите категорию:\n1 - Работа\n2 - Личное\n3 - Обучение ")
        category = input("\nВыбор: ")
        if category not in ("1", "2", "3"):
            print(f"{'-' * 40}\nОШИБКА! Категория не определена\n{'-' * 40}")
            continue
        break

    # Получает название категории по ключу
    # Ключ-это номер категории, значение-название категории
    category = get_category(category)

    print("\nСрок выполнения задачи\n")
    while True:
        year = input("Введите год: ")
        is_digit(year)

        #
        if year:
            if int(year) < 2024:
                print(f"{'-' * 40}\nОШИБКА! Ушли те времена\n{'-' * 40}")
                continue
        else:
            print(
                f"{'-' * 40}\nnОШИБКА! Нужно вводить цифры.Попробуйте ещё раз\n{'-' * 40}"
            )
            continue
        break
    while True:
        #
        month = input("Введите месяц: ")
        if is_digit(month):
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
        #
        day = input("Введите день: ")
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

    period_execution = f"{year}-{month}-{day}"

    while True:
        # Выбрать приоритет для задачи
        print("Выберите приоритет задачи:\n1 - Низкий\n2 - Средний\n3 - Высокий ")
        priority = input("\nВыбор: ")
        if priority not in ("1", "2", "3"):
            print(f"{'-' * 40}\nОШИБКА! Приоритет не определён\n{'-' * 40}")
            continue
        break
    priority = get_priority(priority)

    if update:
        return (
            name,
            description,
            category,
            period_execution,
            priority,
        )

    task_manager.add_task(
        name,
        description,
        category,
        period_execution,
        priority,
    )


def delete_task_handler():
    while True:
        # ID задачи
        book_id = input("Введите ID задачи для удаления: ")

        # Функция is_digit(book_id) проверяет, состоит ли ввод для id задачи только из цифр.
        # Если id является числом, вызвать метод удаления задачи.
        if not is_digit(book_id):
            print(f"{'-' * 40}\nОШИБКА! Только числа\n{'-' * 40}")
            continue

        task_manager.delete_task(int(book_id))
        break


def search_task_hendler():
    while True:
        print(
            "ВЫБЕРИТЕ ПАРАМЕТРЫ ПОИСКА:\n1 - По ключевым словам\n2 - По статусу выполнения"
        )
        choice_search = input("\nВыбор: ")

        if choice_search not in ("1", "2"):
            print(f"{'-' * 40}\nОШИБКА! параметры поиска не определены\n{'-' * 40}")
            continue

        if choice_search == "1":
            keywords = input("Введите слова через пробел: ").split()

            if len(max(keywords)) <= 2:
                print(
                    f"{'-' * 40}\nС такими словами, рузультат поиска может отличаться от ожидаемого"
                )

            task_manager.search(keywords=keywords)
            return

        elif choice_search == "2":
            print("Выберите статус для поиска:\n1 - Выполнена\n2 - Не выполнена")
            status = input("\nВыбор: ")
            if status not in ("1", "2"):
                print(f"{'-' * 40}\nОШИБКА! Категория не определена\n{'-' * 40}")
                continue

            # Получает название статуса по ключу
            # Ключ-это номер статуса, значение-статус
            status = get_status(status)

            # Вызывает метод поиска передаёт название статуса
            task_manager.search(status=status)
            return


def display_all_task_hendler():
    task_manager.display_all_task()


def display_categories_hendler():
    while True:
        # получить символический номер категории
        print("Выберите категорию:\n1 - Работа\n2 - Личное\n3 - Обучение ")
        num_category = input("\nВыбор: ")

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


def update_task_handler(update_status: bool = False):
    tasks = task_manager.get_tasks()
    while True:
        print(f"{'-' * 40}\nВЫБЕРИТЕ ID ЗАДАЧИ ИЗ СПИСКА:\n")
        # tasks = [task for task in tasks ]
        for task in tasks:
            print(f"{task.name} | ID:{task.id}")
        task_id = input("Введите ID: ")
        if is_digit(task_id):
            if update_status:
                task_manager.update_status(int(task_id))
                break

            task_manager.update_task(int(task_id))
            break
        print(f"{'-' * 40}\nОШИБКА! Здесь нет таких ID{'-' * 40}\n")
        continue
