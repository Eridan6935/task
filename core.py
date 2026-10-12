def create_task(tasks, name):
    if not name or not name.strip():
        return False
    tasks.append(name.strip())
    return True


def edit_task(tasks, number, new_name):
    if number < 1 or number > len(tasks) or not new_name.strip():
        return False
    tasks[number - 1] = new_name.strip()
    return True


def delete_task(tasks, number):
    if number < 1 or number > len(tasks):
        return False
    del tasks[number - 1]
    return True
