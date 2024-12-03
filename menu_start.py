from task_manager import TaskManager
from write_read import write_read_file
from menu_dict import MENU_OPTIONS


def main() -> None:
    # Вызов функции для работы с файлами (чтение или запись)
    # Призапуске программы, создаются объекты задач из данных файла
    write_read_file(task_manager_class=TaskManager, choices="r")

    while True:
        print(f"\nМЕНЮ УПРАВЛЕНИЯ:\n{'-' * 40}")

        # Вывод всех доступных опций меню
        # Опции записаны в словаре модуля - menu_dict.py
        for key, option in MENU_OPTIONS.items():
            print(f"{key}. {option['label']}")

        print("0. Выход")
        print("-" * 40)

        choice = input("Выберите действие: ")
        print()

        # Если выбран пункт из меню
        if choice in MENU_OPTIONS:
            MENU_OPTIONS[choice]["action"]()
        elif choice == "0":
            print("Программа завершена.")
            break
        # Если пользователь ввел неверный выбор
        else:
            print(f"{'-' * 40}\nОШИБКА! Неверный выбор. Попробуйте снова.\n{'-' * 40}")


main()
