# Завдання 3: Статистика продажів
def calculate_sell(sell):
    total_value = {}
    for item in sell:
        good_name = item["продукт"]
        quantity = item["кількість"]
        price = item["ціна"]
        value = quantity * price

        if good_name in total_value:
            total_value[good_name] += value
        else:
            total_value[good_name] = value

    return total_value

# Дані про продажі
sell = [
    {"продукт": "мандарин", "кількість": 10, "ціна": 5},
    {"продукт": "слива", "кількість": 20, "ціна": 3},
    {"продукт": "мандарин", "кількість": 5, "ціна": 5},
    {"продукт": "мандарин", "кількість": 50, "ціна": 100},
    {"продукт": "помідори", "кількість": 15, "ціна": 4},
    {"продукт": "слива", "кількість": 100, "ціна": 10},
    {"продукт": "кава", "кількість": 30, "ціна": 25},
    {"продукт": "шоколад", "кількість": 80, "ціна": 15},
]

print("Завдання 3: Статистика продажів")
print(" Вхідні дані ")
print("Список продажів:")
for i, sale in enumerate(sell, 1):
    value = sale["кількість"] * sale["ціна"]
    print(f"{i}. {sale['продукт']}: {sale['кількість']} x {sale['ціна']} = {value} грн")

# Обчислюємо загальний дохід
total_sell_value = calculate_sell(sell)
print(f"\n Результати обчислення ")
print("Загальний дохід за продуктом:", total_sell_value)

# Виводимо детальну статистику
print("\nДетальна статистика доходу:")
total_revenue = 0
for product, revenue in total_sell_value.items():
    print(f"  {product}: {revenue} грн")
    total_revenue += revenue

print(f"\nЗагальний дохід від усіх продажів: {total_revenue} грн")

# Створення списку продуктів, що принесли дохід більший ніж 1000
list_for_goods = []
for good in total_sell_value:
    if total_sell_value[good] > 1000:
        list_for_goods.append(good)

print(f"\n Високоприбуткові продукти ")
print("Продукти з доходом більше 1000 грн:", list_for_goods)