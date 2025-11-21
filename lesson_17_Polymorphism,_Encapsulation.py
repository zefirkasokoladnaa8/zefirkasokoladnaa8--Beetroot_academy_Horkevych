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
# === 1. Клас Author ===
import datetime
class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
    
        self.books = [] 

    def __str__(self):
        return f"Автор: {self.name} ({self.country})"
    
    def __repr__(self):
        return f"Author(name='{self.name}', birthday='{self.birthday}')"
    
        
# === 2. Клас Book ===
class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        
        # 1. Перевірка типу
        if not isinstance(author, Author):
            raise ValueError("Автор має бути об'єктом Author")
        
        # 2. Присвоєння
        self.author = author 

        # 3. Логика лічильника та списку
        Book.total_books += 1
        author.books.append(self)

    def __str__(self):
        return f"Книга: '{self.name}' ({self.year})"
    
    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year})"
    

# === 3. Клас Library ===
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return f'Бібліотека: {self.name}'
    
    def __repr__(self):
        return f'Бібліотека {self.name}'
    
    def new_book(self, name, year, author):
        # Створюємо нову книгу
        new_book_obj = Book(name, year, author)
        
        # Добавляемо в список книг бібліотеки
        self.books.append(new_book_obj)

        # Добавляем автора, якщо його ще немає
        if author not in self.authors:
            self.authors.append(author)

        return new_book_obj
    
    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]


# === ТЕСТУВАННЯ ===

print('---1. Тестуємо Author---')
author1 = Author('Alexandre Duma', 'France', datetime.date(1802, 7, 24))
print(author1) 
print(repr(author1))

print('\n---2. Тестуємо Book---')
# Створюємо книги напряму (без бібліотеки), щоб перевірити клас Book
book1 = Book('Three Musketeers', 1844, author1)
book2 = Book('The Count of Monte Cristo', 1844, author1)

print(book1)
print(f'Загальна кількість книг (Book.total_books): {Book.total_books}')
# Перевіряємо, чи додалися книги до списку автора
print(f'Книги автора {author1.name}: {author1.books}') 

print('\n---3. Тестуємо Library---')
library1 = Library('Центральна міська бібліотека')
print(library1)

# Додаємо ще книги через бібліотеку
library1.new_book('Twenty Years After', 1845, author1)

print(f"Всього книг в бібліотеці: {len(library1.books)}")
print(f"Всього авторів в бібліотеці: {len(library1.authors)}")

# Перевіряємо, що лічильник Book врахував і книги створені вручну, і через бібліотеку
print(f"Загальний лічильник Book.total_books: {Book.total_books}")

# -----------------------------------------------------------------------------------------------------------------------------------


