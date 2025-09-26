#Task 1. The greeting program.
#Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
#"Good day <name>! <day> is a perfect day to learn some python.

# Method 1: f-string 
name = 'Anna'
day = 'friday'
greeting_1 = (f"Good day {name}! {day} is a perfect day to learn some python.")
print(greeting_1)

# Method 2: str.format()
greeting_2 = "Good day {}! {} is a perfect day to learn some python."
print(greeting_2.format(name, day))

# Method 3: str.format() with index
greeting_3 = "Good day {0}! {1} is a perfect day to learn some python."
print(greeting_3.format(name, day))

# Method 4: % operator
greeting_4 = "Good day %s! %s is a perfect day to learn some python." % (name, day) 
print(greeting_4)

# Method 5: str.join() or string concatenation
greeting_5 = "Good day " + name + "! " + day + " is a perfect day to learn some python."
print(greeting_5)


#Task 2. Manipulate strings.
#Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.
first_name = 'Anna'
last_name = 'Horkevych'
full_name = first_name + ' ' + last_name
print(full_name)


#Task 3.Using python as a calculator.
a = 9
b = 2
print(a + b) #addition
print(a - b) #subtraction
print(a / b) #division
print(a * b) #multiplication
print(a ** b) #exponent (power)
print(a % b) #modulus
print(a // b) #floor division

