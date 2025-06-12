import re
def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}
    total_lines = 0
    processed_lines = 0

    try:
        # Читаємо вхідний файл
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                total_lines += 1
                # Витягуємо IP-адресу з початку рядка (перше слово до пробілу)
                ip_match = re.match(r'^(\d+\.\d+\.\d+\.\d+)', line.strip())

                if ip_match:
                    ip_address = ip_match.group(1)
                    processed_lines += 1

                    # Перевіряємо, чи IP-адреса є в списку дозволених
                    if ip_address in allowed_ips:
                        if ip_address in ip_counts:
                            ip_counts[ip_address] += 1
                        else:
                            ip_counts[ip_address] = 1

        print(f"Оброблено {processed_lines} рядків з {total_lines} загальних рядків.")
        print(f"Знайдено {len(ip_counts)} дозволених IP-адрес.")
        # Записуємо результати у вихідний файл
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write("Результати аналізу дозволених IP-адрес:\n")

            if ip_counts:
                # Сортуємо IP-адреси за кількістю входжень (від більшого до меншого)
                sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

                total_allowed_requests = sum(ip_counts.values())

                for ip, count in sorted_ips:
                    percentage = (count / total_allowed_requests) * 100
                    line = f"{ip} - {count} входжень ({percentage:.1f}%)\n"
                    output_file.write(line)

                output_file.write(f"\nЗагальна кількість запитів від дозволених IP: {total_allowed_requests}\n")
                output_file.write(f"Кількість унікальних дозволених IP: {len(ip_counts)}\n")
            else:
                output_file.write("Дозволених IP-адрес не знайдено в лог-файлі.\n")

        print(f"Результати збережено у файл '{output_file_path}'")

    except FileNotFoundError:
        print(f"Помилка: Вхідний файл '{input_file_path}' не знайдено!")
    except IOError as e:
        print(f"Помилка вводу/виводу: {e}")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

def main():
    print("Фільтр IP-адрес з лог-файлу")
    # Список дозволених IP-адрес
    allowed_ips = [
        "83.149.9.216",
        "192.168.1.1",
        "10.0.0.1",
        "110.136.166.128",
        "203.0.113.1",
        "198.51.100.1",
        "91.177.205.119",
        "71.212.224.97",
        "172.16.0.1",
        "66.249.73.135"
    ]
    # Назви файлів
    input_file = "apache_logs.txt"
    output_file = "filtered_ips_results.txt"

    print(f"Список дозволених IP-адрес ({len(allowed_ips)} адрес):")
    for i, ip in enumerate(allowed_ips, 1):
        print(f"  {i}. {ip}")

    print(f"\nАналіз файлу: {input_file}")
    print(f"Результати будуть збережені у: {output_file}")
    # Викликаємо функцію фільтрації
    filter_ips(input_file, output_file, allowed_ips)

if __name__ == "__main__":
    main()