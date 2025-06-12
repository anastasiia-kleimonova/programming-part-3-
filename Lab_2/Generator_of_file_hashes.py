import hashlib
import os
def generate_file_hashes(*file_paths):
    file_hashes = {}

    for file_path in file_paths:
        try:
            # Відкриваємо файл у бінарному режимі
            with open(file_path, 'rb') as file:
                # Створюємо об'єкт SHA-256 хешу
                sha256_hash = hashlib.sha256()
                # Читаємо файл частинами (щоб не завантажувати великі файли повністю в пам'ять)
                chunk_size = 8192
                while chunk := file.read(chunk_size):
                    sha256_hash.update(chunk)
                # Отримуємо хеш у шістнадцятковому форматі
                file_hash = sha256_hash.hexdigest()
                file_hashes[file_path] = file_hash

                print(f" Хеш для '{file_path}' обчислено успішно.")

        except FileNotFoundError:
            print(f" Помилка: Файл '{file_path}' не знайдено!")
            file_hashes[file_path] = None

        except IOError:
            print(f" Помилка: Не вдалося прочитати файл '{file_path}'!")
            file_hashes[file_path] = None

        except Exception as e:
            print(f" Несподівана помилка з файлом '{file_path}': {e}")
            file_hashes[file_path] = None

    return file_hashes

def get_file_size(file_path):
    """Отримує розмір файлу в байтах"""
    try:
        return os.path.getsize(file_path)
    except:
        return 0

def format_file_size(size_bytes):
    """Форматує розмір файлу для читабельного виводу"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / (1024 ** 2):.1f} MB"
    else:
        return f"{size_bytes / (1024 ** 3):.1f} GB"

def main():
    print("Генератор SHA-256 хешів файлів")
    # Приклад використання з декількома файлами
    files_to_hash = [
        "apache_logs.txt",
        "log_file.txt"
    ]

    print(f"Обчислення хешів для {len(files_to_hash)} файлів:")
    # Генеруємо хеші
    results = generate_file_hashes(*files_to_hash)

    print("\nРезультати:")

    for file_path, file_hash in results.items():
        file_size = get_file_size(file_path)
        formatted_size = format_file_size(file_size)

        print(f"Файл: {file_path}")
        print(f"Розмір: {formatted_size}")

        if file_hash:
            print(f"SHA-256: {file_hash}")
        else:
            print("SHA-256: Не вдалося обчислити")

if __name__ == "__main__":
    main()