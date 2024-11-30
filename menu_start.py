from check import is_digit
from dict_for_search import (
    checking_month,
    get_category,
    get_priority,
    get_status,
)
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
        print("3. Найти задачи")
        print("4. Показать все ")
        print("5. Показать задачи по категориям ")
        print("6. Редактировать ")
        print("0. Выход")
        print("-" * 40)
        choice = input("Выберите действие: ")
        print()

        # Ввести данные для новой задачи
        if choice == "1":
            # Заголов для задачи
            while True:
                name = input("Введите название: ")

                # Проверить поле на наличие символов
                if len(name.replace(" ", "")) == 0:
                    print(
                        f"{'-' * 40}\nОШИБКА! Поле 'name' не может быть пустым\n{'-' * 40}"
                    )

                    continue
                break
            while True:
                description = input("Введите описание: ")

                # Проверить поле описание на наличие символов
                if len(description.replace(" ", "")) == 0:
                    print(
                        f"{'-' * 40}\nПоле 'description' не может быть пустым\n{'-' * 40}"
                    )
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

            print("Срок выполнения")
            while True:
                year = input("Введите год: ")
                is_digit(year)

                #
                if year:
                    if int(year) < 2024:
                        print("Ушли те времена")
                        continue
                else:
                    print("Нужно вводить цифры.Попробуйте ещё раз")
                    continue
                break
            while True:
                #
                month = input("Введите месяц: ")
                if is_digit(month):
                    if int(month) < 1 or int(month) > 12:
                        print("Этот месяц не отсюда. Попробуйте ещё раз.")
                        continue
                else:
                    print("Так не пойдёт, нужны цифры")
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
                        print("Эти дни нам не знакомы.Попробуйте ещё раз")
                        continue
                else:
                    print("Непонятно, что за день ")
                    continue
                break

            period_execution = f"{year}-{month}-{day}"

            while True:
                # Выбрать приоритет для задачи
                print(
                    "Выберите приоритет задачи:\n1 - Низкий\n2 - Средний\n3 - Высокий "
                )
                priority = input("\nВыбор: ")
                if priority not in ("1", "2", "3"):
                    print(f"{'-' * 40}\nОШИБКА! Приоритет не определён\n{'-' * 40}")
                    continue
                break
            priority = get_priority(priority)

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
                "ВЫБЕРИТЕ ПАРАМЕТРЫ ПОИСКА:\n1 - По ключевым словам\n2 - По статусу выполнения"
            )
            choice_search = input("\nВыбор: ")

            if choice_search not in ("1", "2"):
                print(f"{'-' * 40}\nОШИБКА! параметры поиска не определены\n{'-' * 40}")
                continue

            if choice_search == "1":
                keywords = input("Введите слова через пробел: ").split()
                task_manager.search(keywords=keywords)

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

        # Показать все задачи
        elif choice == "4":
            task_manager.display_all_task()

        # Показать задачи в выбранной категории
        elif choice == "5":

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

            # Получает название категории по ключу
            # Ключ-это номер категории, значение-название категории
            category = get_category(num_category)

            # Вызывает метод показа задач в выбранной категории
            # Передаёт название категории
            # task_manager.display_tasks_in_category(category)
            task_manager.search(category=category)

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
