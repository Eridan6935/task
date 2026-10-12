import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            return data
        print("Предупреждение: файл задач имеет неверный формат. Загружен пустой список.")
    except (OSError, json.JSONDecodeError) as error:
        print(f"Не удалось загрузить задачи: {error}")
    return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        return True
    except OSError as error:
        print(f"Не удалось сохранить задачи: {error}")
        return False
