# from menu_handler import create_task_handler
from dict_for_compare import get_status
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
    ) -> None:
        """
        Создаёт новую задачу и добавляет её в список.

        Задача добавляется в список 'list_tasks' и записывается в файл.
        """
        # Создаёт оъект задачи
        task = Task(name, description, category, period_execution, priority)

        # Заносит объек задачи в список задач
        self.list_tasks.append(task)

        # Вызывает функцию записи в файл
        # Передаёт список задач.Флаг "w" для записи по-умолчанию.
        write_read_file(self.list_tasks, task_manager_class=TaskManager)

    def get_tasks(self) -> list:
        """Метод возвращает список всех задач, хранящихся в атрибуте 'list_tasks' бъекта"""

        return self.list_tasks

    def delete_task(self, task_id: int) -> None:
        """
        Удалить задачу по её ID.

        Этот метод ищет задачу с заданным ID в списке задач 'list_tasks'. Если задача с таким ID найдена,
        она удаляется из списка и сохраняется в файл.
        В случае, если задача с таким ID не найдена, выводится сообщение об ошибке.

        Args:
            task_id (int): ID задачи, которую нужно удалить.
        """
        for task in self.list_tasks:
            if task.id == task_id:
                self.list_tasks.remove(task)
                print(f"\nЗАДАЧА С ID:'{task_id}' УДАЛЕНА\n{'-'*40}")

                # Запись в файл обновлённого списка задач
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
        """
        Перенаправляет поиск задач в соответствующий метод в зависимости от переданных аргументов.

        Этот метод выполняет проверку на наличие переданных аргументов и вызывает соответствующие
        методы для поиска задач:
        - Если передан параметр 'category', вызывается метод 'search_by_category' для поиска по категории.
        - Если передан параметр 'status', вызывается метод 'search_by_status' для поиска по статусу.
        - Если передан параметр 'keywords', вызывается метод 'search_by_keywords' для поиска по ключевым словам.

        """
        # Если задан параметр category, перенаправляем на поиск по категории
        if category is not None:
            self.search_by_category(category)

        # Если задан параметр status, перенаправляем на поиск по статусу
        elif status is not None:
            print(status)
            self.search_by_status(status)

        # Если задан параметр keywords, перенаправляем на поиск по ключевым словам
        elif keywords is not None:
            self.search_by_keywords(keywords)

    def search_by_category(self, category: str) -> None:
        """
        Перебирает все задачи, и выводит информацию
        о каждой задаче определенной категории. Если в данной категории нет задач,
        выводится сообщение о том, что задачи в категории отсутствуют.
        """
        if not self.list_tasks:
            # Если список задач пуст, выводим сообщение и завершаем выполнение метода
            print(f"\nСПИСОК ЗАДАЧ ПУСТ.\n{'='*40}")
            return
        # Создаем список задач, отфильтрованных по категории
        tasks = [
            task
            for task in self.list_tasks
            if task.category.lower().replace(" ", "") == category.lower()
        ]

        if len(tasks) == 0:
            # Если в выбранной категории нет задач, выводим сообщение об этом
            print(f"\nВ КАТЕГОРИИ {category.upper()} НЕТ ЗАДАЧ.\n{'-'*40}")
            return
        # Если задачи найдены, выводим их список
        print(f"\nСПИСОК ВСЕХ ЗАДАЧ В КАТЕГОРИИ - {category.upper()}:\n{'-'*40}")
        # Выводим все задачи
        print(*tasks, sep="\n")

    def search_by_status(self, status: str = None):
        """Ищет задачи по статусу и выводит их"""

        if status is not None:
            # Фильтруем задачи, оставляя только те, у которых статус совпадает с переданным
            tasks = [task for task in self.list_tasks if task.status == status]
            if len(tasks) > 0:
                # Если задачи с таким статусом найдены, выводим их список
                print(f"\nЗАДАЧИ СО СТАТУСОМ '{status}':\n{'-' * 40}")
                print(*tasks, "\n")  # Выводим все задачи

            else:
                # Если задачи с таким статусом не найдены, выводим сообщение об ошибке
                print(f"\nЗАДАЧИ СО СТАТУСОМ '{status}' НЕ НАЙДЕНЫ\n{'-' * 40}")

    def search_by_keywords(self, keywords: list) -> None:
        """
        Ищет задачи, содержащие ключевые слова в названии или описании.

        - Перебирает все задачи из списка 'self.list_tasks'.
        - Проверяет, содержится ли хотя бы одно из ключевых
          слов в названии или описании задачи.
        - Если есть совпадения, выводит найденные задачи.
        - Если совпадений нет, уведомляет пользователя.
        """
        # Список для хранения задач
        tasks = []
        for task in self.list_tasks:
            for key in keywords:

                # Проверяет совпадение ключевого слова с названием
                # или описанием задачи (без учёта регистра)
                if (
                    key.lower() in task.name.lower()
                    or key.lower() in task.description.lower()
                ):
                    tasks.append(task)
        # Если задачи найдены, выводит результаты поиска
        if len(tasks) > 0:
            print(f"РЕЗУЛЬТАТЫ ПОИСКА:\n{'-' * 40}")
            print(*tasks, sep="\n")
        else:
            print(f"{'-' * 40}\nПОИСК НЕ ДАЛ РЕЗУЛЬТАТА")

    def update_task(self, task_id: int = None):
        """
        Обновляет задачу с указанным ID.

        Метод ищет задачу по переданному ID. Если задача найдена,
        вызывается функция для ввода новых данных задачи. После обновления
        данных задача сохраняется в файл. Если задача с указанным ID не найдена,
        выводится сообщение об ошибке.
        """
        # Отложенный импорт функции для обработки обновления задачи
        from menu_handler import create_task_handler

        # Ищем задачу с указанным ID
        task = next((task for task in self.list_tasks if task.id == task_id), None)
        if task is not None:
            # Получаем новые данные для задачи
            name, description, category, period_execution, priority = (
                create_task_handler(update=True)
            )
            # Обновляем поля задачи
            task.name = name
            task.description = description
            task.category = category
            task.period_execution = period_execution
            task.priority = priority
            # Сохраняем обновлённый список задач в файл
            write_read_file(self.list_tasks)
        else:
            # Выводим сообщение, если задача с указанным ID не найдена
            print(f"Задача с ID {task_id} не найдена.")

    def update_status(self, task_id: int) -> None:
        """
        Обновляет статус задачи с указанным ID.

        Метод ищет задачу по переданному ID. Если задача найдена, пользователю предлагается выбрать
        новый статус задачи ("Выполнена" или "Не выполнена"). После изменения статуса обновлённые
        данные задачи сохраняются в файл.
        """
        # Ищем задачу по указанному ID
        task = next((task for task in self.list_tasks if task.id == task_id), None)
        if task is not None:

            # Бесконечный цикл для запроса статуса до корректного ввода
            while True:
                print("Выберите для обновления:")
                # Вывод вариантов выбора статуса
                for key, val in get_status().items():
                    print(f"{key}. {val}")

                new_status = input("\nВыбор: ")

                # Проверка выбора по словарю
                if new_status not in get_status():
                    print(f"{'-' * 40}\nОШИБКА! Статус не определен\n{'-' * 40}")
                    continue
                break

            # Получает название статуса по ключу
            # Ключ-это номер статуса, значение-статус
            new_status = get_status(new_status)
            # Устанавливает объекту задачи новый статус
            task.status = new_status
            print(f"Новый статус задачи с ID:{task.id} - {task.status}")
            # Записывает изменения в файл
            write_read_file(self.list_tasks)
        else:
            print(f"{'-' * 40}\nОШИБКА! Задача с ID:{task_id} не найдена")
