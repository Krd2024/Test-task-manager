from main import TaskManager


task_manager = TaskManager()
# task_test = ("Дело", "Очень важное", "Работа", 3, "Высокий")
# for i in range(5):
#     task_manager.add_task(
#         "Дело",
#         "Описание, важного, дела",
#         "Работа",
#         "3 дня",
#         "Высокий",
#     )
task_manager.add_task(
    "Дело",
    "Описание, важного, дела",
    "Работа",
    "3 дня",
    "Высокий",
)
task_manager.add_task(
    "Дело",
    "Описание, важного, дела",
    "Работа",
    "3 дня",
    "Высокий",
)
task_manager.display_all_task()
# task_manager.display_tasks_in_category(category="РабоТА")
