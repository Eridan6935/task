"""
История улучшений Task Manager:
0.0.1 — создан главный цикл и консольное меню.
0.0.2 — добавлено отображение списка задач.
0.0.3 — добавлено создание задач.
0.0.4 — добавлено редактирование задач.
0.0.5 — добавлено удаление задач.
0.0.6 — добавлены подтверждения действий.
0.0.7 — добавлено сохранение задач в JSON.
0.0.8 — добавлена загрузка задач при запуске.
0.0.9 — код разделён на модули view, utils, core и storage.
0.1.0 — обработаны некорректный ввод и ошибки чтения/записи файла.
"""

from view import show_menu, show_tasks, show_message
from core import create_task, edit_task, delete_task
from storage import load_tasks, save_tasks
from utils import check_confirm


def main():
    """Запускает консольный менеджер задач."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            name = input("Введите название задачи: ").strip()
            if create_task(tasks, name):
                if save_tasks(tasks):
                    show_message("Задача добавлена и сохранена.")
                else:
                    show_message("Задача добавлена, но сохранить её не удалось.")
            else:
                show_message("Название задачи не может быть пустым.")

        elif choice == "3":
            show_tasks(tasks)
            number = read_task_number("Номер задачи для редактирования: ")
            if number is None:
                continue
            new_name = input("Новое название задачи: ").strip()
            if not check_confirm("Сохранить изменения?"):
                show_message("Редактирование отменено.")
                continue
            if edit_task(tasks, number, new_name):
                if save_tasks(tasks):
                    show_message("Задача изменена и сохранена.")
                else:
                    show_message("Изменение выполнено, но сохранить файл не удалось.")
            else:
                show_message("Не удалось изменить задачу. Проверьте номер и название.")

        elif choice == "4":
            show_tasks(tasks)
            number = read_task_number("Номер задачи для удаления: ")
            if number is None:
                continue
            if not check_confirm("Удалить задачу?"):
                show_message("Удаление отменено.")
                continue
            if delete_task(tasks, number):
                if save_tasks(tasks):
                    show_message("Задача удалена и изменения сохранены.")
                else:
                    show_message("Задача удалена, но сохранить файл не удалось.")
            else:
                show_message("Задачи с таким номером нет.")

        elif choice == "5":
            if check_confirm("Выйти из приложения?"):
                show_message("До свидания!")
                break

        else:
            show_message("Неизвестная команда. Выберите пункт от 1 до 5.")


def read_task_number(prompt):
    """Безопасно читает номер задачи."""
    try:
        number = int(input(prompt).strip())
        if number < 1:
            show_message("Номер задачи должен быть положительным.")
            return None
        return number
    except ValueError:
        show_message("Ошибка: введите номер целым числом.")
        return None


if __name__ == "__main__":
    main()
