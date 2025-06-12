import hashlib
class User:
    """Базовий клас користувача"""
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = True

    def _hash_password(self, password):
        """Створює хеш пароля для безпеки"""
        return hashlib.md5(password.encode()).hexdigest()

    def verify_password(self, password):
        """Перевіряє правильність введеного пароля"""
        return self.password_hash == self._hash_password(password)

    def __str__(self):
        return f"Користувач: {self.username}, Активний: {self.is_active}"

class Administrator(User):
    """Клас адміністратора з розширеними правами"""
    def __init__(self, username, password):
        super().__init__(username, password)
        self.permissions = ["читання", "запис", "видалення", "адміністрування"]
        self.role = "Адміністратор"

    def get_permissions(self):
        """Повертає список дозволів адміністратора"""
        return self.permissions

    def __str__(self):
        return f"Адміністратор: {self.username}, Дозволи: {', '.join(self.permissions)}"

class RegularUser(User):
    """Клас звичайного користувача"""
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None
        self.role = "Звичайний користувач"

    def update_last_login(self):
        """Оновлює дату останнього входу"""
        from datetime import datetime
        self.last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        login_info = f", Останній вхід: {self.last_login}" if self.last_login else ""
        return f"Звичайний користувач: {self.username}{login_info}"

class GuestUser(User):
    """Клас гостьового користувача з обмеженими правами"""
    def __init__(self, username, password):
        super().__init__(username, password)
        self.permissions = ["читання"]
        self.role = "Гість"

    def get_permissions(self):
        """Повертає обмежені дозволи гостя"""
        return self.permissions

    def __str__(self):
        return f"Гість: {self.username}, Дозволи: {', '.join(self.permissions)}"

class AccessControl:
    """Клас для управління доступом та користувачами"""
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """Додає нового користувача до системи"""
        if user.username in self.users:
            print(f"Помилка: Користувач '{user.username}' вже існує!")
            return False

        self.users[user.username] = user
        print(f"Користувач '{user.username}' успішно доданий до системи!")
        return True

    def authenticate_user(self, username, password):
        """Перевіряє логін та пароль користувача"""
        if username not in self.users:
            print("Помилка: Користувач не знайдений!")
            return None

        user = self.users[username]

        if not user.is_active:
            print("Помилка: Обліковий запис деактивований!")
            return None

        if user.verify_password(password):
            print(f"Успішний вхід! Привіт, {username}!")
            # Оновлюємо дату входу для звичайних користувачів
            if isinstance(user, RegularUser):
                user.update_last_login()
            return user
        else:
            print("Помилка: Неправильний пароль!")
            return None

    def list_users(self):
        """Показує список всіх користувачів"""
        if not self.users:
            print("Система порожня. Користувачів немає.")
            return

        print("\n СПИСОК КОРИСТУВАЧІВ ")
        for user in self.users.values():
            print(user)

    def deactivate_user(self, username):
        """Деактивує користувача"""
        if username in self.users:
            self.users[username].is_active = False
            print(f"Користувач '{username}' деактивований.")
        else:
            print("Користувач не знайдений!")

def show_menu():
    """Показує головне меню"""
    print("  СИСТЕМА УПРАВЛІННЯ КОРИСТУВАЧАМИ")
    print("1. Додати адміністратора")
    print("2. Додати звичайного користувача")
    print("3. Додати гостя")
    print("4. Увійти в систему")
    print("5. Переглянути всіх користувачів")
    print("6. Деактивувати користувача")
    print("7. Вийти")


def main():
    """Головна функція програми"""
    access_control = AccessControl()

    while True:
        show_menu()
        choice = input("Виберіть опцію (1-7): ").strip()

        if choice == "1":
            username = input("Введіть ім'я адміністратора: ").strip()
            password = input("Введіть пароль: ").strip()
            if username and password:
                admin = Administrator(username, password)
                access_control.add_user(admin)
            else:
                print("Помилка: Введіть ім'я та пароль!")

        elif choice == "2":
            username = input("Введіть ім'я користувача: ").strip()
            password = input("Введіть пароль: ").strip()
            if username and password:
                user = RegularUser(username, password)
                access_control.add_user(user)
            else:
                print("Помилка: Введіть ім'я та пароль!")

        elif choice == "3":
            username = input("Введіть ім'я гостя: ").strip()
            password = input("Введіть пароль: ").strip()
            if username and password:
                guest = GuestUser(username, password)
                access_control.add_user(guest)
            else:
                print("Помилка: Введіть ім'я та пароль!")

        elif choice == "4":
            username = input("Введіть ім'я користувача: ").strip()
            password = input("Введіть пароль: ").strip()
            user = access_control.authenticate_user(username, password)
            if user:
                print(f"Тип користувача: {user.role}")
                if hasattr(user, 'get_permissions'):
                    print(f"Ваші дозволи: {', '.join(user.get_permissions())}")

        elif choice == "5":
            access_control.list_users()

        elif choice == "6":
            username = input("Введіть ім'я користувача для деактивації: ").strip()
            access_control.deactivate_user(username)

        elif choice == "7":
            print("До побачення!")
            break

        else:
            print("Помилка: Виберіть правильну опцію (1-7)!")

        input("\nНатисніть Enter для продовження...")

if __name__ == "__main__":
    main()