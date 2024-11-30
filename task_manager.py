from task import Task
from write_read import write_read_file


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

        # Заносит объек задачи в список задач
        self.list_tasks.append(task)

        # Вызывает функцию записи в файл
        # Передаёт список задач и флаг "w" для записи
        write_read_file(self.list_tasks, task_manager_class=TaskManager)

    def delete_task(self, task_id):
        for task in self.list_tasks:
            if task.id == task_id:
                self.list_tasks.remove(task)
                print(f"\nЗАДАЧА '{task.name}' УДАЛЕНА\n{'-'*40}")

                write_read_file(self.list_tasks, task_manager_class=TaskManager)
                return
        print(f"ОШИБКА! ЗАДАЧА С ID: {task_id} НЕ НАЙДЕНА.\n{'-'*40}")

    def display_all_task(self) -> None:
        """
        Перебирает все задачи, и выводит информацию
        о каждой задаче. Если список пуст, выводится сообщение о том, что задачи отсутствуют.
        """
        if not self.list_tasks:
            print("\nНЕТ ЗАДАЧ\n")
            return

        print(f"\nСПИСОК ВСЕХ ЗАДАЧ:\n{'='*40}")
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
            print(f"\nСПИСОК ЗАДАЧ ПУСТ.\n{'='*40}")
            return

        tasks = [
            task
            for task in self.list_tasks
            if task.category.lower().replace(" ", "") == category.lower()
        ]

        if len(tasks) == 0:
            print(f"\nВ КАТЕГОРИИ {category.upper()} НЕТ ЗАДАЧ.\n{'-'*40}")
            return

        print(f"\nСПИСОК ВСЕХ ЗАДАЧ В КАТЕГОРИИ - {category.upper()}:\n{'-'*40}")
        print(*tasks, sep="\n")

    def search_by_status(self, status: str = None):

        if status is not None:
            tasks = [task for task in self.list_tasks if task.status == status]
            if len(tasks) > 0:

                print(f"\nЗАДАЧИ СО СТАТУСОМ '{status}':\n{'-' * 40}")
                print(*tasks, "\n")

            else:
                print(f"\nЗАДАЧИ СО СТАТУСОМ '{status}' НЕ НАЙДЕНЫ\n{'-' * 40}")

    def search_by_keywords(self, keywords: list) -> None:

        # print("==================")
        print()
        tasks = []
        for task in self.list_tasks:
            for key in keywords:
                if (
                    key.lower() in task.name.lower()
                    or key.lower() in task.description.lower()
                ):
                    # print(task)
                    tasks.append(task)
        if len(tasks) > 0:
            print(f"РЕЗУЛЬТАТЫ ПОИСКА:\n{'-' * 40}")
            print(*tasks, sep="\n")
        else:
            print(f"{'-' * 40}\nПОИСК НЕ ДАЛ РЕЗУЛЬТАТА")