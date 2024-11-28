class Task:
    count_id = 0

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
    ):
        task = Task(name, description, category, period_execution)
        self.list_tasks.append(task)
