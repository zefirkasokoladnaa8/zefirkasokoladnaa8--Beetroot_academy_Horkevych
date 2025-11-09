#Task 1 A Person class

# Make a class called Person. Make the __init__() method take firstname, lastname, 
# and age as parameters and add them as attributes. 
# Make another method called talk() which makes prints a greeting from the person containing, 
# for example like this: "Hello, my name is Carl Johnson and I’m 26 years old".

class Person:
    def __init__(self, firstname, lastname,age ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
      
    def called_talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')
        
person1 = Person('Bill', 'Klinton', 79)
person1.called_talk()

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Task 2 Doggy age
# Create a class Dog with class attribute 'age_factor' equals to 7. 
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dogs_name, dogs_age):
        self.dogs_name = dogs_name
        self.dogs_age = dogs_age

    def human_age_equivalent(self):
        return self.dogs_age * self.age_factor
      
    
dog1 = Dog('Tuzik', 5)
print(dog1.human_age_equivalent())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------





