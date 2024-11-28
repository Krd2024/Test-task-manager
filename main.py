def write_read_file(tasks: list = None, choices: str = "w") -> None:
    """
    Функция для записи или чтения данных о книгах в/из файла "tasks.csv".

    Аргументы:
        tasks (list, optional): Список задач.
        choices (str, optional): Режим работы с файлом.

    - Если 'choices' равно "w", функция записывает
        информацию о задачах  в файл "tasks.csv"
        (id, name, description, category, period_execution,priority,status).

    - Если 'choices' отличается от "w", функция читает строки из файла,
        обрабатывает их и добавляет задачи в объект.

    Исключения:
        - При чтении файла: если строка в файле не соответствует
          ожидаемому формату, выводится сообщение "Нет записи".

    """
    task = TaskManager()

    with open("tasks.csv", choices, encoding="utf-8") as file:
        if choices == "w":
            for task in tasks:
                file.write(
                    f"{task.id},{task.name},{task.description},"
                    f"{task.category},{task.period_execution},"
                    f"{task.priority},{task.status}\n"
                )
        else:
            try:
                for line in file:
                    (
                        id,
                        name,
                        description,
                        category,
                        period_execution,
                        priority,
                        status,
                    ) = line.strip().split(",")
            except ValueError:
                print("Нет данных")


class Task:
    """
    Класс для представления задачи.

    Счетчик уникальных идентификаторов (count_id)
    увеличивается автоматически при создании каждой новой задачи.
    """

    count_id = 1

    def __init__(
        self,
        name: str,
        description: str,
        category: str,
        period_execution: int,
        priority: str,
        status: str = "Не выполнена",
    ) -> None:
        self.id = Task.count_id
        self.name = name
        self.category = category
        self.description = description
        self.period_execution = period_execution
        self.status = status
        self.priority = priority
        Task.count_id += 1

    def __str__(self):
        """Строковое представление задачи"""

        return (
            f"----- {self.name.upper()} -----\n"
            f"Категория: {self.category}\n"
            f"Описание: {self.description}\n"
            f"Срок выполнения: {self.period_execution}\n"
            f"Приоритет: {self.priority}\n"
            f"Статус: {self.status}\n"
        )


class TaskManager:
    list_tasks = []  # Список всех задач

    def add_task(
        self,
        name: str,
        description: str,
        category: str,
        period_execution: int,
        priority: str,
    ):
        """
        Создаёт новую задачу и добавляет её в список.

        Задача добавляется в список 'list_tasks' и записывается в файл.
        """
        # Создаёт оъект задачи
        task = Task(name, description, category, period_execution, priority)
        # Заносит объек задачи в список задач
        self.list_tasks.append(task)
        # Вызывает функцию записи в файл
        # Передаёт список задач и флаг для "w" для записи
        write_read_file(self.list_tasks, choices="w")

    def display_all_task(self) -> None:
        """
        Перебирает все задачи, и выводит информацию
        о каждой задаче. Если список пуст, выводится сообщение о том, что задачи отсутствуют.
        """
        if not self.list_tasks:
            print("Нет задач")
            return

        print("\n СПИСОК ВСЕХ ЗАДАЧ:")
        print(" " * 6)
        for task in self.list_tasks:
            print(task)

    def display_tasks_in_category(self, category):
        """
        Перебирает все задачи, и выводит информацию
        о каждой задаче определенной категории. Если в данной категории нет задач,
        выводится сообщение о том, что задачи в категории отсутствуют.
        """
        if not self.list_tasks:
            print("\nСПИСОК ЗАДАЧ ПУСТ.\n")
            return

        tasks = [
            task
            for task in self.list_tasks
            if task.category.lower() == category.lower()
        ]
        if len(tasks) == 0:
            print(f"\nВ КАТЕГОРИИ {category.upper()} НЕТ ЗАДАЧ.\n")
            return
        print(f"\nСПИСОК ВСЕХ ЗАДАЧ В КАТЕГОРИИ - {category.upper()}:\n")
        print(*tasks, sep="\n")
