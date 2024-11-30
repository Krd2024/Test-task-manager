from dict_for_compare import get_category, get_status
from task_manager import TaskManager


task_manager = TaskManager()


def search_hendler():
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


def display_all_hendler():
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
