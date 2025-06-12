import sqlite3
import hashlib
class UserManager:
    def __init__(self, db_name="users.db"):
        """Ініціалізація менеджера користувачів"""
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Створення бази даних і таблиці користувачів"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Створення таблиці користувачів
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            conn.commit()
            conn.close()
            print(f"База даних '{self.db_name}' успішно ініціалізована!")

        except sqlite3.Error as e:
            print(f"Помилка при створенні бази даних: {e}")

    def hash_password(self, password):
        """Хешування пароля за допомогою SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self):
        """Додавання нового користувача"""
        print("\n Додавання нового користувача ")

        login = input("Введіть логін: ").strip()
        if not login:
            print("Логін не може бути пустим!")
            return

        password = input("Введіть пароль: ")
        if not password:
            print("Пароль не може бути пустим!")
            return

        full_name = input("Введіть повне ПІБ: ").strip()
        if not full_name:
            print("ПІБ не може бути пустим!")
            return

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Хешування пароля
            hashed_password = self.hash_password(password)
            # Додавання користувача
            cursor.execute('''
                INSERT INTO users (login, password, full_name)
                VALUES (?, ?, ?)
            ''', (login, hashed_password, full_name))

            conn.commit()
            conn.close()

            print(f"Користувач '{login}' успішно додан!")

        except sqlite3.IntegrityError:
            print(f"Помилка: Користувач з логіном '{login}' вже існує!")
        except sqlite3.Error as e:
            print(f"Помилка при додаванні користувача: {e}")

    def update_password(self):
        """Оновлення пароля користувача"""
        print("\n Оновлення пароля ")

        login = input("Введіть логін користувача: ").strip()
        if not login:
            print("Логін не може бути пустим!")
            return
        # Перевірка існування користувача
        if not self.user_exists(login):
            print(f"Користувач з логіном '{login}' не знайдений!")
            return

        old_password = input("Введіть поточний пароль: ")
        # Перевірка поточного пароля
        if not self.verify_password(login, old_password):
            print("Неправильний поточний пароль!")
            return

        new_password = input("Введіть новий пароль: ")
        if not new_password:
            print("Новий пароль не може бути пустим!")
            return

        confirm_password = input("Підтвердіть новий пароль: ")
        if new_password != confirm_password:
            print("Паролі не збігаються!")
            return

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Хешування нового пароля
            hashed_password = self.hash_password(new_password)
            # Оновлення пароля
            cursor.execute('''
                UPDATE users SET password = ? WHERE login = ?
            ''', (hashed_password, login))

            conn.commit()
            conn.close()

            print(f"Пароль для користувача '{login}' успішно оновлено!")

        except sqlite3.Error as e:
            print(f"Помилка при оновленні пароля: {e}")

    def authenticate_user(self):
        """Перевірка автентифікації користувача"""
        print("\n Автентифікація користувача ")

        login = input("Введіть логін: ").strip()
        if not login:
            print("Логін не може бути пустим!")
            return

        password = input("Введіть пароль: ")

        if self.verify_password(login, password):
            # Отримання інформації про користувача
            user_info = self.get_user_info(login)
            if user_info:
                print(f"\n Автентифікація успішна!")
                print(f"Вітаємо, {user_info['full_name']}!")
                print(f"Дата реєстрації: {user_info['created_at']}")
            else:
                print(" Автентифікація успішна!")
        else:
            print(" Неправильний логін або пароль!")

    def user_exists(self, login):
        """Перевірка існування користувача"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute('SELECT COUNT(*) FROM users WHERE login = ?', (login,))
            count = cursor.fetchone()[0]

            conn.close()
            return count > 0

        except sqlite3.Error as e:
            print(f"Помилка при перевірці користувача: {e}")
            return False

    def verify_password(self, login, password):
        """Перевірка пароля користувача"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            # Отримання хешу пароля з БД
            cursor.execute('SELECT password FROM users WHERE login = ?', (login,))
            result = cursor.fetchone()

            conn.close()

            if result:
                stored_hash = result[0]
                input_hash = self.hash_password(password)
                return stored_hash == input_hash

            return False

        except sqlite3.Error as e:
            print(f"Помилка при перевірці пароля: {e}")
            return False

    def get_user_info(self, login):
        """Отримання інформації про користувача"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT login, full_name, created_at 
                FROM users WHERE login = ?
            ''', (login,))

            result = cursor.fetchone()
            conn.close()

            if result:
                return {
                    'login': result[0],
                    'full_name': result[1],
                    'created_at': result[2]
                }
            return None

        except sqlite3.Error as e:
            print(f"Помилка при отриманні інформації користувача: {e}")
            return None

    def show_all_users(self):
        """Показати всіх користувачів (для адміністрування)"""
        print("\n Список всіх користувачів ")

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute('SELECT login, full_name, created_at FROM users ORDER BY created_at')
            users = cursor.fetchall()

            conn.close()

            if users:
                print(f"{'№':<3} {'Логін':<15} {'ПІБ':<25} {'Дата реєстрації':<20}")
                for i, user in enumerate(users, 1):
                    print(f"{i:<3} {user[0]:<15} {user[1]:<25} {user[2]:<20}")
            else:
                print("Користувачі не знайдені.")

        except sqlite3.Error as e:
            print(f"Помилка при отриманні списку користувачів: {e}")

def show_menu():
    """Відображення головного меню"""
    print("      СИСТЕМА УПРАВЛІННЯ КОРИСТУВАЧАМИ")
    print("1. Додати нового користувача")
    print("2. Оновити пароль користувача")
    print("3. Автентифікація користувача")
    print("4. Показати всіх користувачів")
    print("5. Вийти з програми")

def main():
    """Головна функція програми"""
    print("Ласкаво просимо до системи управління користувачами!")
    # Ініціалізація менеджера користувачів
    user_manager = UserManager()

    while True:
        show_menu()

        try:
            choice = input("Виберіть опцію (1-5): ").strip()

            if choice == '1':
                user_manager.add_user()
            elif choice == '2':
                user_manager.update_password()
            elif choice == '3':
                user_manager.authenticate_user()
            elif choice == '4':
                user_manager.show_all_users()
            elif choice == '5':
                print("\nДякуємо за використання програми! До побачення!")
                break
            else:
                print("Невірний вибір! Будь ласка, введіть число від 1 до 5.")

        except KeyboardInterrupt:
            print("\n\nПрограму перервано користувачем. До побачення!")
            break
        except Exception as e:
            print(f"Виникла несподівана помилка: {e}")
        # Пауза перед наступною ітерацією
        input("\nНатисніть Enter для продовження...")

if __name__ == "__main__":
    main()