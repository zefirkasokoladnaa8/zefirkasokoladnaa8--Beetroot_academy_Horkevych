# Task 1

# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

'''Функція oops визиває помиллку IndexError'''
def oops():
    raise IndexError("This is an IndexError!")
'''Функція catch_error ловить помилку із функції oops '''
def catch_error():
    try:
        oops()
    except IndexError as e:
        print('Caught an IndexError:', e)

catch_error()

# Оскільки блок except обробляє лише IndexError,
# він не перехопить KeyError,
# і програма завершиться з винятком KeyError.


# Task 2

# Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
# and then returns the value of squared a divided by b, 
# construct a try-except block which catches an exception 
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero). 

def square_and_divide():
    try:
        a = float(input('Enter number a: '))
        b = float(input('Enter number a: '))
        result = (a**2) / b 
        return round(result, 3)
    except  ZeroDivisionError:
        return 'Error: Division by zero is not allowed.'
    except ValueError:
        return 'Error:  Please enter valid numbers.'

print(square_and_divide())
    
