from menu_handler import (
    create_task_handler,
    delete_task_handler,
    display_all_task_hendler,
    display_categories_hendler,
    search_task_hendler,
    update_task_handler,
)

# Словарь, который используется для отображения опций в меню
# и привязки к ним соответствующих обработчиков.
MENU_OPTIONS = {
    "1": {"label": "Добавить задачу", "action": create_task_handler},
    "2": {"label": "Удалить задачу", "action": delete_task_handler},
    "3": {"label": "Найти задачи", "action": search_task_hendler},
    "4": {"label": "Показать все задачи", "action": display_all_task_hendler},
    "5": {
        "label": "Показать задачи по категориям",
        "action": display_categories_hendler,
    },
    "6": {"label": "Редактировать задачу", "action": update_task_handler},
    "7": {
        "label": "Изменить статус задачи",
        "action": lambda: update_task_handler(update_status=True),
    },
}
