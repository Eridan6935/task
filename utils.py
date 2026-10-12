def check_confirm(message):
    while True:
        answer = input(f"{message} (д/н): ").strip().lower()
        if answer in ("д", "да", "y", "yes"):
            return True
        if answer in ("н", "нет", "n", "no"):
            return False
        print("Введите «д» для подтверждения или «н» для отмены.")
