# Task 1 A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print "My favorite movie is named {name}".  

def favorite_movie(name):
    print(f"My favorite movie is named {name}")
favorite_movie("Pirates of the Caribbean")

# ----------------------------------------------------------------------------------------------------------------
# Task 2 Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(name, capital):
    country = {'name': name, 'capital': capital}
    return country

print(make_country('Ukraine', 'Kyiv'))
# ----------------------------------------------------------------------------------------------------------------

# Task 3 A simple calculator.
# Create a function called make_operation, 
# which takes in a simple arithmetic operator as a first parameter 
# (to keep things simple let it only be '+', '-' or '*') 
# and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter.
#  For example:
# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42  

def make_operation(operator, *args):   # *args - довільна кількість аргументів
    if operator == '+':                # якщо оператор +
        return sum(args)               # повертаємо суму аргументів
    elif operator == '-':              # якщо оператор -
        return args[0] - sum(args[1:]) # повертаємо різницю першого аргументу і суми решти аргументів
    elif operator == '*':              # якщо оператор *
        result = 1                     # результат = 1
        for num in args:               # для кожного аргументу (ітеруємо)
            result *= num              # множимо result на аргумент
        return result                  # повертаємо добуток всіх аргументів
    else:
        return "Invalid operator"      # якщо інший опреатор повертаємо повідомлення про помилку
    
print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6, 9))
print(make_operation('/', 7, 68, 2))



