# Task 1
# Method overloading.

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def talk(self):
        print('woof woof')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print('meow')

def make_it_talk(animal_object):
    animal_object.talk()

dog1 = Dog('Bobik')
cat1 = Cat('Murka')

make_it_talk(dog1)
make_it_talk(cat1)
# ----------------------------------------------------------------------------------------------


# Task 2
# Library










