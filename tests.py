import pytest
from unittest.mock import patch
from menu_handler import create_task_handler
from task_manager import TaskManager

task_manager = TaskManager()


# Фикстура для подготовки ввода данных
@pytest.fixture
def task_inputs():
    return [
        "Задача 1",  # Название
        "Описание задачи",  # Описание
        "2",  # Категория
        "2023",  # Некорректный год
        "2024",  # Корректный год
        "abc",  # Некорректный месяц
        "13",  # Некорректный месяц
        "11",  # Корректный месяц
        "33",  # Некорректный день
        "02",  # Корректный день
        "3",  # Приоритет ('Высокий')
        # ВТОРАЯ ЗАДАЧА
        "Задача 2",  # Название
        "Описание задачи 2",  # Описание
        "2",  # Категория
        "202.5",  # Некорректный год
        "2025",  # Корректный год
        "5 5",  # Некорректный месяц
        "1 3",  # Некорректный месяц
        "1 2",  # Корректный месяц
        "3 3",  # Некорректный день
        "2",  # Корректный день
        "3",  # Приоритет ('Высокий')
    ]


# Фикстура для мокирования функции print
@pytest.fixture
def mock_print():
    """
    Эта фикстура используется для замены стандартной функции print на мок-объект,
    который перехватывает все вызовы print в тестах. Это позволяет тестировать вывод
    программы, не отображая его в консоли, а проверяя, какие именно сообщения были
    переданы в print.
    """
    with patch("builtins.print") as mock:
        yield mock


def test_task_creation(task_inputs, mock_print):
    """
    Тест для проверки создания задач с обработкой некорректных вводов.
    Используется мокирование вывода print для перехвата сообщений.
    """

    # Мокирует функцию input, заменяя её на заранее заданные значения из task_inputs.
    # side_effect задаёт список значений, которые будут возвращаться при каждом вызове input.
    with patch("builtins.input", side_effect=task_inputs):
        create_task_handler()  # Вызываем обработчик создания задачи для первой задачи
        create_task_handler()  # Вызываем обработчик создания задачи для второй задачи

        # Проверка вывода
        # Собрать все аргументы, переданные в print, в список printed_output.
        printed_output = [call.args[0] for call in mock_print.call_args_list]

        # Проверяем, что программа уведомляет об ошибках
        assert any(
            f"{'-' * 40}\nОШИБКА! Ушли те времена\n{'-' * 40}" in line
            for line in printed_output
        )
        assert any(
            f"{'-' * 40}\nnОШИБКА! Этот месяц не отсюда. Попробуйте ещё раз.\n{'-' * 40}"
            in line
            for line in printed_output
        )
        assert any(
            f"{'-' * 40}\nnОШИБКА! Эти дни нам не знакомы.Попробуйте ещё раз\n{'-' * 40}"
            in line
            for line in printed_output
        )

        # Проверяем, что задачи были созданы
        created_tasks = task_manager.get_tasks()
        assert len(created_tasks) == 2

        # Проверяет корректность данных для первой задачи
        task_1 = created_tasks[0]
        assert task_1.name == "Задача 1"
        assert task_1.description == "Описание задачи"
        assert task_1.category == "Личное"
        assert task_1.period_execution == "2024-11-02"
        assert task_1.priority == "Высокий"

        # Проверяет корректность данных для второй задачи
        task_2 = created_tasks[1]
        assert task_2.name == "Задача 2"
        assert task_2.description == "Описание задачи 2"
        assert task_2.category == "Личное"
        assert task_2.period_execution == "2025-12-2"
        assert task_2.priority == "Высокий"


def test_search_task():
    """
    Тест на поиск задач по ключевым словам.

    В данном тесте проверяется, что метод search_by_keywords корректно выполняет поиск задач
    по ключевым словам и выводит информацию о задачах, которые соответствуют поисковым запросам.

    Шаги:
    1. Мокаем функцию print, чтобы перехватить вывод.
    2. Запускаем метод поиска задач по ключевым словам.
    3. Собираем все строки, переданные в print, и проверяем, что задачи с нужными ключевыми словами
       отображаются в выводе.
    4. Проверяем, что задачи с названиями "ЗАДАЧА 1" и "ЗАДАЧА 2" присутствуют в выводе.
    """

    with patch("builtins.print") as mock_print:  # Мокаем функцию print
        args = ["Описание", "задачи"]  # Ключевые слова для поиска
        task_manager.search_by_keywords(args)  # Вызываем поиск задач по ключевым словам
        printed_output = []  # Список для хранения перехваченных строк вывода

        # Перебираем вызовы print, чтобы собрать их аргументы
        for call in mock_print.call_args_list:
            if call.args:
                printed_output.append(" ".join(str(arg) for arg in call.args))

    printed_output = [
        " ".join(map(str, call.args)) for call in mock_print.call_args_list
    ]

    # Проверяем, что в выводе присутствуют строки с названиями задач "ЗАДАЧА 1" и "ЗАДАЧА 2"
    assert any("ЗАДАЧА 1" in line for line in printed_output)
    assert any("ЗАДАЧА 2" in line for line in printed_output)
    print("\nПоиск по ключевым словам прошёл успешно!")


def get_printed_output(mock_print):
    """Собирает и возвращает вывод из всех вызовов print."""

    return [" ".join(map(str, call.args)) for call in mock_print.call_args_list]


def test_delete_task_not_found():
    """
    Тестирует ситуацию, когда попытка удаления задачи с несуществующим ID
    приводит к выводу сообщения об ошибке.

    В этом тесте проверяется, что метод удаления задачи 'delete_task' корректно
    обрабатывает ситуацию, когда задача с указанным ID не существует в списке задач.
    Ожидается, что программа выведет сообщение об ошибке с соответствующим текстом.
    """
    with patch("builtins.print") as mock_print:
        task_id = 3
        task_manager.delete_task(task_id)
        printed_output = get_printed_output(mock_print)
        expected_message = "ОШИБКА! ЗАДАЧА С ID: 3 НЕ НАЙДЕНА.\n----------------------------------------"
        assert printed_output[0] == expected_message
    print("\nУдаление по несуществующему ID обработано успешно!")


def test_delete_task_successful():
    """
    Тестирует успешное удаление задачи по ID.

    Тест проверяет, что метод удаления задачи 'delete_task' работает правильно
    и удаляет задачу по указанному ID. Тест проверяет, что после выполнения удаления
    выводится корректное сообщение о том, что задача была удалена.

    """

    with patch("builtins.print") as mock_print:
        task_id = 1
        task_manager.delete_task(task_id)
        printed_output = get_printed_output(mock_print)
        expected_message = f"\nЗАДАЧА С ID:'{task_id}' УДАЛЕНА\n{'-' * 40}"
        assert printed_output[0] == expected_message
    print("\nУдаление по ID завершено успешно!")


# =================================================================


# =================================================================


# @pytest.fixture
# def task_manager_with_tasks():
#     """Создает менеджер задач с несколькими задачами."""
#     task_manager = TaskManager()

#     # Добавляем задачи

#     task_manager.add_task(
#         "Купить продукты",
#         "Список: молоко, хлеб, яйца",
#         "Личное",
#         "2024-12-31",
#         "Низкий",
#     )
#     task_manager.add_task(
#         "Сдать отчет",
#         "Финансовый отчет за квартал",
#         "Работа",
#         "2024-12-15",
#         "Высокий",
#     )
#     task_manager.add_task(
#         "Посетить врача",
#         "Обследование у стоматолога",
#         "Личное",
#         "2024-11-30",
#         "Средний",
#     )

#     return task_manager
