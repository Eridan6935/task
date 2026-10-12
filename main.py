from view import show_menu, show_tasks, show_message
from core import create_task, edit_task, delete_task
from storage import load_tasks, save_tasks
from utils import check_confirm


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            name = input("Введите название задачи: ").strip()
            if name:
                create_task(tasks, name)
                save_tasks(tasks)
                show_message("Задача добавлена.")
            else:
                show_message("Название не может быть пустым.")
        elif choice == "3":
            show_tasks(tasks)
            try:
                number = int(input("Номер задачи для редактирования: "))
                new_name = input("Новое название: ").strip()
                if check_confirm("Сохранить изменения?"):
                    if edit_task(tasks, number, new_name):
                        save_tasks(tasks)
                        show_message("Задача изменена.")
                    else:
                        show_message("Не удалось изменить задачу. Проверьте номер и название.")
            except ValueError:
                show_message("Введите номер целым числом.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                number = int(input("Номер задачи для удаления: "))
                if check_confirm("Удалить задачу?"):
                    if delete_task(tasks, number):
                        save_tasks(tasks)
                        show_message("Задача удалена.")
                    else:
                        show_message("Задачи с таким номером нет.")
            except ValueError:
                show_message("Введите номер целым числом.")
        elif choice == "5":
            if check_confirm("Сохранить изменения и выйти?"):
                save_tasks(tasks)
                show_message("До свидания!")
                break
        else:
            show_message("Неизвестная команда. Выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main()
