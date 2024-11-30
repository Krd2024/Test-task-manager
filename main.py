from write_read import write_read_file


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
        period_execution: str,
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
            f"----- {self.name.upper()}({self.id}) -----\n"
            f"- ID:{self.id} -\n"
            f"Категория: {self.category}\n"
            f"Описание: {self.description}\n"
            f"Срок выполнения: {self.period_execution}\n"
            f"Приоритет: {self.priority}\n"
            f"Статус: {self.status}\n\n"
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
        status: str = "Не выполнена",
    ):
        """
        Создаёт новую задачу и добавляет её в список.

        Задача добавляется в список 'list_tasks' и записывается в файл.
        """
        # Создаёт оъект задачи
        task = Task(name, description, category, period_execution, priority)
        # write_read_file_2(task, choices="a")
        print(task, "<<<<<<<<<<<< ")

        # Заносит объек задачи в список задач
        self.list_tasks.append(task)

        # Вызывает функцию записи в файл
        # Передаёт список задач и флаг "w" для записи
        write_read_file(self.list_tasks, task_manager_class=TaskManager)

    def delete_task(self, task_id):
        for task in self.list_tasks:
            if task.id == task_id:
                self.list_tasks.remove(task)
                print(f"\nЗадача '{task.name}' удалена\n")

                write_read_file(self.list_tasks, task_manager_class=TaskManager)
                return
        print(f"ОШИБКА! Задача с ID: {task_id} не найдена.\n")

    def display_all_task(self) -> None:
        """
        Перебирает все задачи, и выводит информацию
        о каждой задаче. Если список пуст, выводится сообщение о том, что задачи отсутствуют.
        """
        if not self.list_tasks:
            print("\nНЕТ ЗАДАЧ\n")
            return

        print("\n СПИСОК ВСЕХ ЗАДАЧ:")
        tasks = [task for task in self.list_tasks]
        print(*tasks, sep="\n")

    def search(self, category: str = None, status: str = None, keywords: str = None):

        if category is not None:
            self.search_by_category(category)

        elif status is not None:
            print(status)
            self.search_by_status(status)

        elif keywords is not None:
            self.search_by_keywords(keywords)

    def search_by_category(self, category) -> None:
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
            if task.category.lower().replace(" ", "") == category.lower()
        ]

        if len(tasks) == 0:
            print(f"\nВ КАТЕГОРИИ {category.upper()} НЕТ ЗАДАЧ.\n")
            return

        print(f"\nСПИСОК ВСЕХ ЗАДАЧ В КАТЕГОРИИ - {category.upper()}:\n")
        print(*tasks, sep="\n")

    def search_by_status(self, status: str = None):

        if status is not None:
            tasks = [task for task in self.list_tasks if task.status == status]
            if len(tasks) > 0:

                print(f"\nЗадачи со статусом '{status}':\n")
                print(*tasks, "\n")

            else:
                print(f"\nЗадачи со статусом '{status}' не найдены\n")

    def search_by_keywords(self, keywords: list) -> None:

        print()
        for task in self.list_tasks:
            for key in keywords:
                if (
                    key.lower() in task.name.lower()
                    or key.lower() in task.description.lower()
                ):
                    print(task)
