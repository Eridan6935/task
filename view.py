def show_menu():
    print("\n=== TASK MANAGER ===")
    print("1 — Посмотреть задачи")
    print("2 — Добавить задачу")
    print("3 — Редактировать задачу")
    print("4 — Удалить задачу")
    print("5 — Выход")


def show_tasks(tasks):
    print("\n--- Список задач ---")
    if not tasks:
        print("Список задач пуст.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def show_message(message):
    print(message)
