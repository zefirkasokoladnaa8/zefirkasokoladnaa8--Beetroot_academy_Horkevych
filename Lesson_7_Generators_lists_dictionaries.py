# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 
some_dict = {}   # Створюємо порожній словник
some_long_sentence = input("Enter a sentence: ")   # Запитуємо користувача на введення речення
some_long_sentence_list = some_long_sentence.lower().split()  # З речення створюємо список слів з маленької літери, split() без аргументів ігнорує всі пробіли 
for word in some_long_sentence_list:  # Ітеруємося по кожному слову у списку і очищаємо слово від знаків пунктуації
    cleaned_word = word.strip(' ,.!?"\n')  # strip видаляє символи з початку та кінця
    if not cleaned_word: # Якщо слово пусте
        continue #Пропускаємо його  

    if cleaned_word in some_dict: # Якщо слово є в словнику, збільшуємо його значення на 1
        some_dict[cleaned_word] += 1
    else: # Якщо слова немає в словнику, додаємо його до словника з значенням 1
        some_dict[cleaned_word] = 1
print(some_dict)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 
# Input data
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_cost = {} #Створюємо порожній словник
for fruit in stock: # Ітеруємося по ключам у словнику stock
    # Так як назви ключів у обох словниках однакові,
    # то перебираючі ключі словника stock ми підставляємо ці ж ключі в словник prices для отримання цін
    # та множимо їх на кількість яблук у stock отримуємо загальну вартість
    total_cost[fruit] = stock[fruit] * prices[fruit] 
print(total_cost)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 3. List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.
result = [(i, i**2) for i in range(1, 11)]

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # Створюємо список з днів тижня
dict_weekdays = {i: day for i, day in enumerate(weekdays, start=1)} # Створюємо словник з днів тижня
print(dict_weekdays)

reverse_dict_weekdays = {day: i for i, day in dict_weekdays.items()} # Створюємо зворотний словник з днів тижня
print(reverse_dict_weekdays)


