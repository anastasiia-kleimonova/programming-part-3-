import re
def analyze_log_file(log_file_path):
    response_codes = {}

    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Пошук HTTP коду відповіді в рядку (наприклад: " 200 " або " 404 ")
                # HTTP код зазвичай знаходиться після методу запиту
                match = re.search(r'" (\d{3}) ', line)

                if match:
                    code = match.group(1)  # Отримуємо код відповіді
                    # Додаємо код до словника або збільшуємо лічильник
                    if code in response_codes:
                        response_codes[code] += 1
                    else:
                        response_codes[code] = 1

    except FileNotFoundError:
        print(f"Помилка: Файл '{log_file_path}' не знайдено!")
        return {}
    except IOError:
        print(f"Помилка: Не вдалося прочитати файл '{log_file_path}'!")
        return {}
    except Exception as e:
        print(f"Несподівана помилка: {e}")
        return {}

    return response_codes

def main():
    # Шлях до лог-файлу
    log_file = "apache_logs.txt"

    print("Аналізатор лог-файлів HTTP сервера")
    # Викликаємо функцію аналізу
    results = analyze_log_file(log_file)

    if results:
        print(f"Результати аналізу файлу '{log_file}':")
        # Сортуємо коди за кількістю входжень (від більшого до меншого)
        sorted_codes = sorted(results.items(), key=lambda x: x[1], reverse=True)

        total_requests = sum(results.values())

        for code, count in sorted_codes:
            percentage = (count / total_requests) * 100
            print(f"Код {code}: {count:,} разів ({percentage:.1f}%)")

        print(f"\nЗагальна кількість запитів: {total_requests:,}")
    else:
        print("Не вдалося проаналізувати файл або файл порожній.")

if __name__ == "__main__":
    main()