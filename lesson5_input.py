#Task 1. The Guessing Game. ------------------------------------------------

import random

computer_number = random.randint(1, 10) # Генеруємо випадкове число від 1 до 10

while True: # Створюємо нескінченний цикл
    user_number = input("Guess the number from 1 to 10: ") # Запитуємо у користувача число
    if user_number.isdigit(): # Перевіряємо чи введено число
        user_number = int(user_number) # Перетворюємо рядок на число
    else: # Якщо введено не число, виводимо повідомлення 
        print("Please enter a valid number.") 
        continue #і повертаємося до початку циклу

    if user_number < 1 or user_number > 10:# Перевіряємо чи введено число в діапазоні від 1 до 10   
        print("Please enter a number between 1 and 10.")# Якщо введено число не в діапазоні від 1 до 10, виводимо повідомлення 
        continue #і повертаємося до початку циклу

    if user_number == computer_number:# Перевіряємо чи вгадане число дорівнює випадковому числу
        print("You guessed the number!")
        break # Якщо вгадане число дорівнює випадковому числу, виходимо з циклу
    else:
        print("You did not guess the number.") # Якщо вгадане число не дорівнює випадковому числу, виводимо повідомлення і повертаємося до початку циклу
#---------------------------------------------------------------------------------

#Task 2. The birthday greeting program.
while True: #Створюємо нескінченний цикл
    name = input("What is your name? ") #Запитуємо ім'я
    age = input("How old are you? ") #Запитуємо вік
    if age.isdigit(): #Перевіряємо чи введені цифри
        age = int(age) #Переводимо в число якщо введені цифри
        print(f"Hello, {name}! On the next birthday you will be {age + 1} years old.") # і Виводимо повідомлення
        break #Закриваємо цикл якщо введені коректні дані
    else: #Інакше
        print("Please enter a valid number.") #Виводимо повідомлення якщо введено не число
        continue #Перезапускаємо цикл   
#------------------------------------------------------------------------------------
#Task 3. Words combination
import random  # Імпортуємо модуль для роботи з випадковістю

word = input("Введіть слово: ") # Запитуємо слово від користувача
# Генеруємо 5 випадкових "слів" з символів введеного рядка
i = 0
while i < 5:  # цикл для створення 5 різних варіацій
    new_word = ''.join(random.sample(word, len(word)))  # random.sample беремо випадкові символи та перемішуємо їх
    print(new_word)
    i += 1
