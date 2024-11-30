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
            f"\n{self.name.upper()}  |  ID:{self.id} \n\n"
            f"Категория: {self.category}\n"
            f"Описание: {self.description}\n"
            f"Срок выполнения: {self.period_execution}\n"
            f"Приоритет: {self.priority}\n"
            f"Статус: {self.status}\n"
            f"{'-' * 40}\n"
        )
