from check import is_digit
from dict_category import get_category_for_menu
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
        print("Меню упрвления задачами:")
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

        # Ввести данные для новой задачи (заголовок,автор,год издания)
        if choice == "1":
            # Заголов для задачи
            name = input("Введите название: ")

            # Проверить поле на наличие символов
            if len(name.replace(" ", "")) == 0:
                print("\nОШИБКА! Поле 'name' не может быть пустым\n")
                continue
            # Имя автора задачи
            description = input("Введите описание:")

            # Проверить поле описание на наличие символов
            if len(description.replace(" ", "")) == 0:
                print("ОШИБКА! Поле 'description' не может быть пустым")
                continue

            category = input("Введите категорию: ")

            if len(category.replace(" ", "")) == 0:
                print("ОШИБКА! Поле 'description' не может быть пустым")
                continue

            period_execution = input("Время на завершение задачи: ")

            if len(period_execution.replace(" ", "")) == 0 and is_digit(
                period_execution
            ):
                print("ОШИБКА! Не корректные данные")
                continue

            priority = input("Введите приоритет: ")

            if len(category.replace(" ", "")) == 0:
                print("ОШИБКА! Поле 'priority' не может быть пустым")
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
                print("-" * 40)
                print("ОШИБКА! Только числа ")
                print("-" * 40)

        # Поиск задачи по названию,автору или году издания
        elif choice == "3":

            query = input("Введите название,автора или год для поиска: ")

            # Проверить ввод на наличие символов
            if len(query.replace(" ", "")) > 0:

                # Вызов метода поиска задачи
                task_manager.search_books(query)
            else:
                print("-" * 40)
                print("ОШИБКА! Поиск не может быть пустым")
                print("-" * 40)

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
                print("-" * 40)
                print("ОШИБКА! Категория не определена")
                print("-" * 40)
                continue
            # else:

            # Получае значение словаря по ключу
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
