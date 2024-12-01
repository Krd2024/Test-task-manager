# from check import is_digit
# from dict_for_compare import (
#     # checking_month,
#     # get_category,
#     # get_priority,
# )
from menu_handler import (
    create_task_handler,
    # delete_handler,
    delete_task_handler,
    # display_all_hendler,
    display_all_task_hendler,
    display_categories_hendler,
    # search_hendler,
    search_task_hendler,
    update_task_handler,
)
from task_manager import TaskManager  # , write_read_file
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
    # task_manager = TaskManager()

    # Вызвать функцию для чтения из файла (выбор действия "r" для чтения)

    write_read_file(task_manager_class=TaskManager, choices="r")

    while True:
        print(f"\nМЕНЮ УПРАВЛЕНИЯ:\n{'-' * 40}")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Найти задачи")
        print("4. Показать все задачи")
        print("5. Показать задачи по категориям ")
        print("6. Редактировать задачу")
        print("7. Изменить статус задачи ")
        print("0. Выход")
        print("-" * 40)
        choice = input("Выберите действие: ")
        print()

        # Ввести данные для новой задачи
        if choice == "1":
            create_task_handler()

        elif choice == "2":
            delete_task_handler()

        elif choice == "3":
            search_task_hendler()

        # Показать все задачи
        elif choice == "4":
            display_all_task_hendler()

        # Показать задачи в выбранной категории
        elif choice == "5":
            display_categories_hendler()

        elif choice == "6":
            update_task_handler()

        elif choice == "7":
            update_task_handler(update_status=True)

        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print(f"{'-' * 40}\nОШИБКА! Неверный выбор. Попробуйте снова.\n{'-' * 40}")


main()
