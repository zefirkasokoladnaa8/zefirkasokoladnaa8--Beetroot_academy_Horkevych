# Task 2 The sys module.

# The “sys.path” list is initialized from the PYTHONPATH environment variable.
# Is it possible to change it from within Python?
# If so, does it affect where Python looks for module files? 
# Run some interactive tests to find it out.

import sys  # імпортуємо модуль sys 

# Подивимось на поточний список шляхів наглядно
print("\nПодивимось на поточний список шляхів наглядно:")

for path in sys.path:                               # ітеруємося по списку шляхів
    print(path)                                     # виводимо шляхи
print(f'Кількість шляхів: {len(sys.path)}')         # виводимо кількість шляхів  
print(f"Перевіримо тип sys.path: {type(sys.path)}") # подивимося на тип об'єкта sys.path (list)

# Тепер перевіримо чи можна змінити список шляхів
print("\nТепер перевіримо чи можна змінити список шляхів:")
print("Спочатку додамо шлях до списку: /tmp/test_modules/mymodule.py")
sys.path.append("/tmp/test_modules/mymodule.py")    # додаємо шлях до списку
print(f'Нова кількість шляхів: {len(sys.path)}')    # виводимо нову кількість шляхів
print(f'Останній шлях: {sys.path[-1]}')             # виводимо останній шлях

print("\nТепер видалимо останній шлях зі списку:")  # виводимо останній шлях
last_path = sys.path.pop()                          # видаляємо останній шлях зі списку і зберігаємо його в змінну last_path

print('\nТепер додамо його вперед в пріорітетне місце:')
sys.path.insert(0,last_path)                               # додаємо останній шлях на перше місце у списку:
print(f'Подивимось обновлений список шляхів: {sys.path}')  # виводимо обновлений список шляхів
print(f'Кількість шляхів: {len(sys.path)}')                # виводимо кількість шляхів

print('\nТепер видалимо перший шлях зі списку:')
sys.path.remove(sys.path[0])                               # видаляємо перший шлях зі списку
print(f'Подивимось кінечний список шляхів: {sys.path}')    # виводимо кінечний список шляхів
print(f'Кількість шляхів: {len(sys.path)}')                # виводимо кількість шляхів

# Висновок:
# Так, список  можна змінити безпосередньо в Python.
# Це впливає на те, де Python шукає модулі.
# Це корисно для тестування, роботи з локальними бібліотеками або нестандартною структурою проєкту.

