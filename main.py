def write_read_file(tasks: list = None, choices: str = "w") -> None:
    task = TaskManager()

    with open("tasks.csv", choices, encoding="utf-8") as file:
        if choices == "w":
            for task in tasks:
                file.write(
                    f"{task.id},{task.name},{task.description},"
                    f"{task.category},{task.period_execution}"
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
        return (
            f"{self.name.upper()}.\n"
            f"Категория: {self.category}\n\n"
            f"Описание:\n{self.description}\n"
            f"Срок выполнения: {self.period_execution}\n\n"
            f"Приоритет: {self.priority}\n"
            f"Статус: {self.status}\n"
        )


class TaskManager:
    list_tasks = []  # Список задач

    def add_task(
        self,
        name: str,
        description: str,
        category: str,
        period_execution: int,
        priority: str,
    ):
        task = Task(name, description, category, period_execution, priority)
        self.list_tasks.append(task)
        write_read_file(self.list_tasks, choices="w")

    def display_output(self) -> None:
        """
        Перебирает все задачи, и выводит информацию
        о каждой задаче. Если список пуст, выводится сообщение о том, что задачи отсутствуют.
        """
        if not self.tasks:
            print("Нет задач")
            return
        print("Список задач:")
        print("***")
        for task in self.tasks:
            print(task)
