from check import is_digit
from dict_for_search import get_category_for_menu, get_status_for_search
from main import TaskManager  # , write_read_file
from write_read import write_read_file


def main() -> None:
    """
    При запуске приложения, читается файл с данными файла.
    Из всех найденых в файле задач, создаются объекты задач с занесением в список.

    Основная функция управления менеджером задач.

    - Добавление задачи.
    - Удаление задачи.
    - Поиск задачи.
    - Просмотр всех задач.
    - Просмотр задач по категория .
    - Обновление статуса задачи.
    - Завершение работы программы.


    """
    # Создаёт объект менеджера задч
    task_manager = TaskManager()

    # Вызвать функцию для чтения из файла (выбор действия "r" для чтения)

    write_read_file(task_manager_class=TaskManager, choices="r")

    while True:
        print("Меню упрвления задачами:\n")
        print("1. Добавить ")
        print("2. Удалить ")
        print("3. Найти ")
        print("4. Показать все ")
        print("5. Выбор категории ")
        print("6. Редактировать ")
        print("0. Выход")
        print("-" * 40)
        choice = input("Выберите действие: ")
        print()

        # Ввести данные для новой задачи
        if choice == "1":
            # Заголов для задачи
            name = input("Введите название: ")

            # Проверить поле на наличие символов
            if len(name.replace(" ", "")) == 0:
                print(
                    f"{'-' * 40}\nОШИБКА! Поле 'name' не может быть пустым\n{'-' * 40}"
                )

                continue

            description = input("Введите описание:")

            # Проверить поле описание на наличие символов
            if len(description.replace(" ", "")) == 0:
                print(
                    f"{'-' * 40}\nПоле 'description' не может быть пустым\n{'-' * 40}"
                )

                continue

            category = input("Введите категорию: ")

            if len(category.replace(" ", "")) == 0:
                print(
                    f"{'-' * 40}\nОШИБКА! Поле 'category' не может быть пустым\n{'-' * 40}"
                )

                continue

            period_execution = input("Время на завершение задачи: ")

            if (
                len(period_execution.replace(" ", "")) == 0
                or 0
                and not is_digit(period_execution)
            ):
                print(f"{'-' * 40}\nОШИБКА! Не корректные данные\n{'-' * 40}")

                continue

            priority = input("Введите приоритет: ")

            if len(category.replace(" ", "")) == 0:
                print(
                    f"{'-' * 40}\nОШИБКА! Поле 'priority' не может быть пустым\n{'-' * 40}"
                )

                continue

            task_manager.add_task(
                name,
                description,
                category,
                period_execution,
                priority,
            )

        elif choice == "2":

            # ID задачи
            book_id = input("Введите ID задачи для удаления: ")

            # Функция is_digit(book_id) проверяет, состоит ли ввод для id задачи только из цифр.
            # Если id является числом, вызвать метод удаления задачи.
            if is_digit(book_id):
                task_manager.delete_task(int(book_id))
                # library.write_file()
            else:
                print(f"{'-' * 40}\nОШИБКА! Только числа\n{'-' * 40}")

                print("ОШИБКА! Только числа ")

        elif choice == "3":
            print(
                "Выберите параметры поиска:\n1 - По ключевым словам\n2 - По статусу выполнения"
            )
            choice_search = input("Выбор: ")

            if choice_search not in ("1", "2"):
                print(f"{'-' * 40}\nОШИБКА! Категория не определена\n{'-' * 40}")
                continue

            if choice_search == "1":
                keywords = input("Введите слова через пробел: ").split()
                task_manager.search_tasks(keywords)

            elif choice_search == "2":
                print("Выберите статус для поиска:\n1 - Выполнена\n2 - Не выполнена")
                status = input("Выбор: ")
                if status not in ("1", "2"):
                    print(f"{'-' * 40}\nОШИБКА! Категория не определена\n{'-' * 40}")
                    continue

                # Получает название статуса по ключу
                # Ключ-это номер статуса, значение-статус
                status = get_status_for_search(status)
                print(status, "<<<<<<<<<< - 2")

                # Вызывает метод поиска передаёт название статуса
                task_manager.search_tasks(status=status)

        # Показать все задачи
        elif choice == "4":
            task_manager.display_all_task()

        # Показать задачи в выбранной категории
        elif choice == "5":

            # получить символический номер категории
            num_category = input(
                "Выберите категорию:\n1 - Работа\n2 - Личное\n3 - Обучение "
            )

            # Если категория не в рамках предложенного, вывести ошибку.
            # Если категория в рамках предложенного,вызвать метод вывода
            # задач выбранной категории
            if num_category not in ("1", "2", "3"):
                # print("-" * 40)
                print(f"{'-' * 40}\nОШИБКА! Категория не определена\n{'-' * 40}")

                # print("-" * 40)
                continue
            # else:

            # Получает название категории по ключу
            # Ключ-это номер категории, значение-название категории
            category = get_category_for_menu(num_category)

            # Вызывает метод показа задач в выбранной категории
            # Передаёт название категории
            task_manager.display_tasks_in_category(category)

        elif choice == "6":
            pass

        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("-" * 40)
            print("ОШИБКА! Неверный выбор. Попробуйте снова.\n")
            print("-" * 40)


main()
