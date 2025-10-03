# Task 1. The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random

random_numbers = []   # імпортуємо random
i = 0   #  Робимо лічильник
while i < 10:   # Генеруємо 10 випадкових чисел за допомогою цикла while 
    random_numbers.append(random.randint(1,100))   # генерируемо випадкове  число від 1 до 100
    i += 1
print('A list of random numbers:', random_numbers)   # Виводимо список на екран 

# Знаходимо найбільше число за допомогою циклу while
largest = random_numbers[0]   # Починаємо з першого елементу
j = 1   # Починаємо з другого елементу

while j < len(random_numbers):   # Поки j менше довжини списку
    if random_numbers[j] > largest:   # Якщо елемент більший за найбільший
        largest = random_numbers[j]   # Оновлюємо найбільший
    j += 1   # Переміщуємося на наступний елемент

print("The largest number in the list:", largest)   # Виводимо найбільший елемент
# ----------------------------------------------------------------------------------------------------

# Task 2 Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random   # імпортуємо random

list1 = []   # Створюємо список 1
list2 = []   # Створюємо список 2
common = []   # Створюємо список 3
i = 0
while i < 10:  # Генеруємо 10 випадкових чисел за допомогою цикла while 
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    i += 1

i = 0
while i < 10:  # Перевіряємо кожен елемент списків
    if list1[i] in list2 and list1[i] not in common:  # Якщо елемент списку 1 є в списку 2 і не є в списку 3
        common.append(list1[i])  # Додаємо елемент в список 3
    i += 1
# Виводимо списки на екран
print("List 1:", list1) 
print("List 2:", list2)
print("Common numbers:", common)


# ----------------------------------------------------------------------------------------------------
# Task 3. Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

result = []   # Створюємо порожній список для збереження результату
i = 1   # Ініціалізуємо лічильник, починаючи з 1
while i <= 100:   # Запускаємо цикл, який буде працювати поки i не перевищить 100
    if i % 7 == 0 and i % 5 != 0:   # Перевіряємо: чи число ділиться на 7 і не ділиться на 5
        result.append(i)   # Якщо умова виконується — додаємо число в кінець списку result
    i += 1   # Збільшуємо лічильник на 1 (переходимо до наступного числа)
print(result)   # Виводимо остаточний список з усіма знайденими числами


