# Завдання 1: Робота з текстом
def count_words(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        # Очищаємо слово від розділових знаків
        word = word.strip('.,!?;:"')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

text = "Дракон без свого вершника - це трагедія. Вершник без свого дракона - це смерть. Стаття перша, розділ перший Кодексу вершника дракона. День Презентації не схожий на жоден інший. Повітря насичене можливостями або навіть і смородом сірки від ображеного дракона. Ніколи не дивіться червоному в очі. Ніколи не відступайте від зеленого. Якщо ви відчуваєте трепет перед коричневим... просто не дивіться. Польовий довідник з різновидів драконів, полковника Каорі."
word_dict = count_words(text)

print("Завдання 1: Підрахунок слів")
print("Вхідний текст:", text)
print("Словник слів:", word_dict)

# Створюємо список слів, що зустрічаються більше 3 разів
frequent_words = []
for word, count in word_dict.items():
    if count > 3:
        frequent_words.append(word)

print("Слова, що зустрічаються більше 3 разів:", frequent_words)

print("\nДетальна статистика:")
for word, count in word_dict.items():
    print(f"'{word}': {count} раз(и)")