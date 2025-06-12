# Завдання 5: Аутентифікація користувачів
import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def check_password(users, login, input_password):
    """Перевіряє введений пароль користувача"""
    if login not in users:
        return False

    hashed_input = hash_password(input_password)
    return users[login]["пароль"] == hashed_input

# Створюємо словник користувачів з зашифрованими паролями
users = {
    "admin": {
        "пароль": hash_password("adminpa456"),
        "піб": "Клеймьонова Анастасія Максимівна"
    },
    "user1": {
        "пароль": hash_password("user1pa123"),
        "піб": "Асламов Єгор Ігорович"
    },
    "user2": {
        "пароль": hash_password("user2pa789"),
        "піб": "Шляхова Наталя Василівна"
    }
}

print("Завдання 5: Аутентифікація користувачів")
print("Доступні користувачі для тестування:")
print("admin (пароль: adminpa456)")
print("user1 (пароль: user1pa123)")
print("user2 (пароль: user2pa789)")
print()

# Демонстрація хешування
print("Приклад хешування пароля:")
example_password = "password"
hashed_example = hash_password(example_password)
print(f"Пароль '{example_password}' → MD5: {hashed_example}")
print()

# Перевірка пароля
print(" Вхід в систему ")
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if check_password(users, login, password):
    print(f" Успішний вхід!")
    print(f"Вітаємо, {users[login]['піб']}!")
else:
    print(" Невірний логін або пароль!")