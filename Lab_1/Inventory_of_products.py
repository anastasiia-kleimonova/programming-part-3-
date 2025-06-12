# Завдання 2: Інвентаризація продуктів
def update_inventory(inventory, product, quantity):

    if product in inventory:
        inventory[product] += quantity
        if inventory[product] < 0:
            inventory[product] = 0
    else:
        # Для нового продукту встановлюємо кількість (не менше 0)
        inventory[product] = quantity if quantity > 0 else 0

    return inventory

def show_inventory(inventory):
    print("Поточний інвентар:")
    for product, quantity in inventory.items():
        print(f"  {product}: {quantity} шт.")

# Створюємо початковий інвентар
inventory = {
    "яблука": 50,
    "персики": 3,
    "печиво": 15,
    "молоко": 2,
    "хліб": 8,
    "рис": 4
}

print("Завдання 2: Інвентаризація продуктів")
print(" Початковий стан ")
show_inventory(inventory)

print("\n Операції з інвентарем ")

# Продали 10 яблук
update_inventory(inventory, "яблука", -10)
print("Продали 10 яблук")

# Додали 20 бананів
update_inventory(inventory, "персики", 20)
print("Додали 20 персиків")

# Додали новий продукт
update_inventory(inventory, "огірки", 25)
print("Додали новий продукт: огірки (25 шт.)")

# Спробували продати більше молока ніж є
update_inventory(inventory, "молоко", -10)
print("Спробували продати 10 пляшок молока (було лише 2)")

print("\n Оновлений стан ")
show_inventory(inventory)

# Створюємо список продуктів з кількістю менше 5
low_stock = []
for product, quantity in inventory.items():
    if quantity < 5:
        low_stock.append(product)

print(f"\n Продукти з кількістю менше 5 ")
print("Продукти, які потрібно поповнити:", low_stock)

# Виводимо детальну інформацію про товари з низьким запасом
print("\nДеталі про товари з низьким запасом:")
for product in low_stock:
    print(f"  {product}: {inventory[product]} шт.")