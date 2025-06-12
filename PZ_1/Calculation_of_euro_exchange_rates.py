import json
import requests
import matplotlib.pyplot as plt
from datetime import datetime
def get_euro_rates():
    """Отримання курсів євро з НБУ"""
    print("Отримання курсів євро з НБУ...")
    # URL для запиту курсів євро за березень 2025
    url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250301&end=20250328&valcode=eur&json"

    try:
        # Виконання запиту до API НБУ
        nbu_response = requests.get(url)
        # Перевірка успішності запиту
        if nbu_response.status_code == 200:
            # Конвертація JSON відповіді
            converted_response = json.loads(nbu_response.content)
            return converted_response
        else:
            print(f"Помилка запиту: {nbu_response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Помилка при отриманні даних: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Помилка при обробці JSON: {e}")
        return None

def display_rates(rates_data):
    """Завдання 1: Виведення дат та курсів на екран"""
    print(" КУРСИ ЄВРО ЗА БЕРЕЗЕНЬ 2025")
    print(f"{'Дата':<12} {'Курс євро (грн)':<15}")
    # Створення списків для зберігання даних для графіка
    dates = []
    rates = []
    # Проходження через кожен елемент у відповіді
    for item in rates_data:
        # Отримання дати та курсу
        date = item['exchangedate']
        rate = item['rate']
        # Виведення на екран
        print(f"{date:<12} {rate:<15}")
        # Збереження для графіка
        dates.append(date)
        rates.append(rate)

    return dates, rates

def create_graph(dates, rates):
    """Завдання 2: Побудова графіка зміни курсу"""
    print("\nПобудова графіка...")
    # Конвертація дат у формат datetime для кращого відображення
    datetime_dates = []
    for date in dates:
        # Конвертація рядка дати у datetime
        dt = datetime.strptime(date, '%d.%m.%Y')
        datetime_dates.append(dt)
    # Налаштування розміру графіка
    plt.figure(figsize=(12, 6))
    # Побудова лінійного графіка
    plt.plot(datetime_dates, rates, marker='o', linewidth=2, markersize=6)
    # Налаштування графіка
    plt.title('Зміна курсу євро (НБУ) - Березень 2025', fontsize=16, fontweight='bold')
    plt.xlabel('Дата', fontsize=12)
    plt.ylabel('Курс (грн за 1 євро)', fontsize=12)
    # Поворот підписів дат для кращої читабельності
    plt.xticks(rotation=45)
    # Сітка для кращої читабельності
    plt.grid(True, alpha=0.3)
    # Автоматичне підлаштування макету
    plt.tight_layout()
    # Відображення графіка
    plt.show()

    print("Графік успішно побудовано!")

def show_statistics(rates):
    """Виведення статистики курсів"""
    print(" СТАТИСТИКА КУРСІВ")

    min_rate = min(rates)
    max_rate = max(rates)
    avg_rate = sum(rates) / len(rates)

    print(f"Мінімальний курс: {min_rate:.4f} грн")
    print(f"Максимальний курс: {max_rate:.4f} грн")
    print(f"Середній курс: {avg_rate:.4f} грн")
    print(f"Різниця: {max_rate - min_rate:.4f} грн")

def main():
    """Головна функція програми"""
    print("Програма для аналізу курсів євро НБУ")
    # Отримання даних з НБУ
    rates_data = get_euro_rates()

    if rates_data is None:
        print("Не вдалося отримати дані. Програма завершена.")
        return

    if len(rates_data) == 0:
        print("Отримано порожній список курсів.")
        return

    print(f"Отримано {len(rates_data)} записів курсів.")
    # Завдання 1: Виведення курсів на екран
    dates, rates = display_rates(rates_data)
    # Показ статистики
    show_statistics(rates)
    # Завдання 2: Побудова графіка
    try:
        create_graph(dates, rates)
    except Exception as e:
        print(f"Помилка при побудові графіка: {e}")
        print("Перевірте, чи встановлено matplotlib: pip install matplotlib")

    print("\nПрограма завершена успішно!")

if __name__ == "__main__":
    main()