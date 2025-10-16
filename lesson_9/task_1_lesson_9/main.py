from greetings import say_hello, say_goodbye # імпортуємо функції з модуля greeting
from calculator import add # імпортуємо функцію з модуля calculator
from calculator import multiply as mult # імпортуємо функцію з модуля calculator і задаємо псевдонім

def main():
    print('---Якась програмка---')

# Використаємо функції із greeting.py
name = input('Введіть ваше ім`я: ')
print(say_hello(name))

# Використаємо функції із calculator.py
num1 = int(input('Введіть перше число: '))
num2 = int(input('Введіть друге число: '))
print(f'{num1} + {num2} = {add(num1, num2)}')
print(f'{num1} * {num2} = {mult(num1, num2)}')

print(say_goodbye(name))

if __name__ == '__main__':
    main()
    
