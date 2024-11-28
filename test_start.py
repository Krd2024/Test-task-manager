from main import TaskManager


task_object = TaskManager()
task_test = ("Дело", "Очень важное", "Работа", 3, "Высокий")
for i in range(5):
    task_object.add_task("Дело", "Очень важное", "Работа", 3, "Высокий")
