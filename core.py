def create_task(tasks, name):
    if not isinstance(name, str) or not name.strip():
        return False
    tasks.append(name.strip())
    return True


def edit_task(tasks, number, new_name):
    if not isinstance(new_name, str) or not new_name.strip():
        return False
    if not isinstance(number, int) or number < 1 or number > len(tasks):
        return False
    tasks[number - 1] = new_name.strip()
    return True


def delete_task(tasks, number):
    if not isinstance(number, int) or number < 1 or number > len(tasks):
        return False
    del tasks[number - 1]
    return True
