# Завдання 4: Система управління задачами
def add_task(tasks, task_name, status="очікує"):
    """Додає нову задачу"""
    tasks[task_name] = status
    print(f" Задача '{task_name}' додана зі статусом '{status}'")
    return tasks

def remove_task(tasks, task_name):
    """Видаляє задачу"""
    if task_name in tasks:
        del tasks[task_name]
        print(f" Задача '{task_name}' видалена")
    else:
        print(f" Задача '{task_name}' не знайдена")
    return tasks

def change_status(tasks, task_name, new_status):
    """Змінює статус задачі"""
    valid_statuses = ["очікує", "в процесі", "виконано"]

    if new_status not in valid_statuses:
        print(f" Невірний статус. Дозволені статуси: {valid_statuses}")
        return tasks

    if task_name in tasks:
        old_status = tasks[task_name]
        tasks[task_name] = new_status
        print(f" Статус задачі '{task_name}' змінено з '{old_status}' на '{new_status}'")
    else:
        print(f" Задача '{task_name}' не знайдена")
    return tasks

def show_tasks(tasks):
    """Виводить всі задачі з їх статусами"""
    if not tasks:
        print("Немає задач у системі")
        return

    print("Поточні задачі:")
    for task, status in tasks.items():
        status_symbol = {"очікує": "", "в процесі": "", "виконано": ""}
        symbol = status_symbol.get(status, "")
        print(f"  {symbol} {task}: {status}")

def get_tasks_by_status(tasks, target_status):
    """Повертає список задач з певним статусом"""
    result = []
    for task, status in tasks.items():
        if status == target_status:
            result.append(task)
    return result

# Створюємо початкові задачі
tasks = {
    "Виконати домашнє завдання": "в процесі",
    "Прибрати в домі": "очікує",
    "Прочитати книгу": "очікує",
    "Сходити на прийом до лікаря": "виконано",
    "Приготувати їжу": "в процесі",
    "Піти на прогулянку з друзями": "очікує"
}

print("Завдання 4: Система управління задачами")
print(" Початковий стан системи ")
show_tasks(tasks)

print("\n Демонстрація функцій ")

# Додаємо нову задачу
print("\n1. Додавання нової задачі:")
add_task(tasks, "Поїхати відпочити на море", "очікує")

# Змінюємо статус існуючої задачі
print("\n2. Зміна статусу задачі:")
change_status(tasks, "Виконати домашнє завдання", "виконано")

# Спробуємо змінити статус неіснуючої задачі
print("\n3. Спроба змінити статус неіснуючої задачі:")
change_status(tasks, "Намалювати картину", "виконано")

# Видаляємо задачу
print("\n4. Видалення задачі:")
remove_task(tasks, "Сходити на прийом до лікаря")

# Спробуємо видалити неіснуючу задачу
print("\n5. Спроба видалити неіснуючу задачу:")
remove_task(tasks, "Намалювати картину")

print("\n Оновлений стан системи ")
show_tasks(tasks)

# Створюємо список задач зі статусом "очікує"
waiting_tasks = get_tasks_by_status(tasks, "очікує")

print(f"\n Задачі зі статусом 'очікує' ")
print("Задачі, що очікують виконання:", waiting_tasks)