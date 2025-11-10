# Task 1

# School

# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student,
# and another one called Teacher. Try to find as many methods 
# and attributes as you can which belong to different classes, 
# and keep in mind which are common and which are not. 
# For example, the name should be a Person attribute, 
# while salary should only be available to the teacher. 


# Базовий клас для всіх людей
class Person:
    def __init__(self, name, age):
        # Ініціалізація загальних атрибутів для всіх людей
        self.name = name
        self.age = age
    
    def __str__(self):
        # Строкове представлення об'єкта
        return f"{self.name}, {self.age}"

# Клас студента, який наслідує від Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # Виклик конструктора батьківського класу
        super().__init__(name, age)
        # Додатковий атрибут, специфічний для студента
        self.student_id = student_id
    
    def __str__(self):
        # Спеціалізоване строкове представлення для студента
        return f"Student: {self.name}, {self.age}, ID: {self.student_id}"

# Клас вчителя, який наслідує від Person
class Teacher(Person):
    def __init__(self, name, age, salary):
        # Виклик конструктора батьківського класу
        super().__init__(name, age)
        # Додатковий атрибут, специфічний для вчителя
        self.salary = salary
    
    def __str__(self):
        # Спеціалізоване строкове представлення для вчителя
        return f"Teacher: {self.name}, {self.age}, Salary: {self.salary}"

# Створення об'єктів різних класів
person = Person("Anna", 30)                    # Об'єкт базового класу
student = Student("Ivan", 20, "12345")         # Об'єкт студента
teacher = Teacher("Alex", 40, 50000)            # Об'єкт вчителя

# Вивід інформації про створені об'єкти
print(person)    # Викликає __str__ для Person
print(student)   # Викликає __str__ для Student  
print(teacher)   # Викликає __str__ для Teacher

# -------------------------------------------------------------------------------------------------------------------------------------------

#  Task 2 Mathematician

class Mathematician:
    def square_nums(self, numbers):
        """Повертає список квадратів чисел"""
        return [x**2 for x in numbers]
    
    def remove_positives(self, numbers):
        """Повертає список без додатних чисел"""
        return [x for x in numbers if x <= 0]
    
    def filter_leaps(self, years):
        """Повертає список лише високосних років"""
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

# Тестування
m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print("Всі тести пройдено успішно!")

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Task 3   Product Store

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
    
    def __repr__(self):
        return f"{self.name} ({self.type}): ${self.price}"

class ProductStore:
    def __init__(self):
        self.products = {}  # {product_name: (product_object, amount)}
        self.income = 0
        self.premium = 0.3  # 30% націнка
    
    def add(self, product, amount):
        """Додає продукт до магазину з націнкою 30%"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        selling_price = product.price * (1 + self.premium)
        
        if product.name in self.products:
            # Оновлюємо кількість існуючого продукту
            existing_product, existing_amount = self.products[product.name]
            self.products[product.name] = (existing_product, existing_amount + amount)
        else:
            # Створюємо новий продукт з ціною продажу
            product_with_premium = Product(product.type, product.name, selling_price)
            self.products[product.name] = (product_with_premium, amount)
    
    def set_discount(self, identifier, percent, identifier_type='name'):
        """Встановлює знижку для продуктів за назвою або типом"""
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        
        discount_factor = (100 - percent) / 100
        
        for product_name, (product, amount) in self.products.items():
            if (identifier_type == 'name' and product.name == identifier) or \
               (identifier_type == 'type' and product.type == identifier):
                # Застосовуємо знижку до поточної ціни
                product.price *= discount_factor
    
    def sell_product(self, product_name, amount):
        """Продає вказану кількість продукту"""
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found")
        
        product, available_amount = self.products[product_name]
        
        if amount > available_amount:
            raise ValueError(f"Not enough '{product_name}'. Available: {available_amount}, requested: {amount}")
        
        # Оновлюємо кількість
        self.products[product_name] = (product, available_amount - amount)
        
        # Додаємо до доходу
        self.income += product.price * amount
        
        # Видаляємо продукт якщо кількість = 0
        if available_amount - amount == 0:
            del self.products[product_name]
    
    def get_income(self):
        """Повертає загальний дохід"""
        return self.income
    
    def get_all_products(self):
        """Повертає інформацію про всі продукти"""
        return {name: (product.type, product.price, amount) 
                for name, (product, amount) in self.products.items()}
    
    def get_product_info(self, product_name):
        """Повертає інформацію про конкретний продукт"""
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found")
        
        product, amount = self.products[product_name]
        return (product.name, amount)

# Тестування
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

print("Всі продукти:", s.get_all_products())

s.sell_product('Ramen', 10)
print("Дохід після продажу:", s.get_income())
print("Інформація про Ramen:", s.get_product_info('Ramen'))

# Перевірка assert
assert s.get_product_info('Ramen') == ('Ramen', 290)
print("✅ Тест пройдено!")

# Додаткові тести
s.set_discount('Ramen', 10)  # 10% знижка на Ramen
print("Після знижки:", s.get_all_products())

s.set_discount('Food', 20, 'type')  # 20% знижка на всі продукти типу Food
print("Після знижки за типом:", s.get_all_products())
