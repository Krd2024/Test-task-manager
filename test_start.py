from main import TaskManager
from write_read import write_read_file


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
write_read_file(task_manager_class=TaskManager, choices="r")
task_manager.display_all_task()
# task_manager.display_tasks_in_category(category="РабоТА")
