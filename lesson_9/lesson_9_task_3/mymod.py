def count_lines(name):
    """ Підраховує кількість рядків у вказаному файлі."""
    try:
        with open (name, 'r', encoding='utf-8') as file:
            return len(file.readlines())
    except FileNotFoundError:
        print(f"Помилка: Файл '{name}' не знайден")
        return 0
    
def count_chars(name):
    """ Підраховує кількість символів у вказаному файлі."""
    try:
        with open(name, 'r', encoding='utf-8') as file:
            return len(file.read())
    except FileNotFoundError:
        print(f"Помилка: Файл '{name}' не знайден.")
        return 0
    
def test(name):
    """ Функція виводить відформатовані результати аналізу вказаного файлу,
    включаючи кількість рядків та загальну кількість символів."""
    print(f"\n--- Аналіз файлу: {name} ---")
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Кількість строк: {lines}")
    print(f"Кількістьо символів: {chars}")

    print("---------------------------------")
