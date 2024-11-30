def write_read_file(
    list_tasks: list = None, task_manager_class: object = None, choices: str = "w"
) -> None:
    """
    Функция для записи или чтения данных о задачах в/из файла "tasks.csv".

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

    if task_manager_class is not None:
        task_manager = task_manager_class()

    with open("tasks.csv", choices, encoding="utf-8") as file:
        print(choices)
        if choices == "w":
            for task in list_tasks:
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

                    task_manager.add_task(
                        name, description, category, period_execution, priority, status
                    )
            except ValueError:
                print("Нет данных")
