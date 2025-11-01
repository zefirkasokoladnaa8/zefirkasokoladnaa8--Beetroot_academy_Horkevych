"""Phonebook application;
Functionality:
    - Add data into database
    - Delete data from database by id
    - Find contact by:
        - name
        - phone number
    - Update contact
    - List all contacts

Data format:
    - phone number
    - name
    - city

DATABASE_FORMAT_EXAMPLE:
{
  "contacts": [
      {
          "phone_number": "123",
          "name": "User",
          "city": "City"
      },
    ]
}
"""
import json
import os.path
import sys # Потрібен для виходу з програми

# --- Імпорт модулів ---
from add_module import add_contact
from edit_module import edit_contact
from find_module import find_contact
from delete_module import delete_contact
from list_module import list_contacts


DEFAULT_DATABASE_NAME = 'phonebook.json'


def validate_user_input(data):
    """Валідація вводу користувача для меню."""
    clean_data = data.strip()
    if not clean_data.isnumeric():
        raise ValueError('Помилка: Введіть номер дії (1-6).')
    
    action_number = int(clean_data)
    
    # Перевіряємо, що вибір в межах 1-6
    if action_number not in [1, 2, 3, 4, 5, 6]:
        raise ValueError('Помилка: Номер дії має бути від 1 до 6.')
    
    return action_number

# Текст головного меню
AVAILABLE_FUNCTIONAL_INFO = """
--- Телефонна книга ---
Будь ласка, оберіть дію:
    1) Додати контакт
    2) Знайти контакт
    3) Оновити контакт
    4) Видалити контакт
    5) Показати всі контакти
    ---
    6) Вихід
"""

def ensure_database(name=DEFAULT_DATABASE_NAME):
    """Створює порожню базу даних, якщо вона не існує."""
    if not os.path.exists(name):
        empty_db = {'contacts': []}
        try:
            with open(name, 'w', encoding='utf-8') as f:
                json.dump(empty_db, f)
            print(f"Створено новий файл бази даних: {name}")
        except IOError as e:
            print(f"Критична помилка: Неможливо створити файл {name}. {e}")
            sys.exit(1) # Вихід, якщо ми не можемо створити БД


# --- Головна логіка програми ---
if __name__ == '__main__':
    # Переконуємось, що JSON файл існує
    ensure_database(DEFAULT_DATABASE_NAME)

    # Головний цикл програми
    while True:
        print(AVAILABLE_FUNCTIONAL_INFO)
        
        try:
            user_input = input("Ваш вибір (1-6): ")
            action_number = validate_user_input(user_input)

            # Обробка вибору користувача
            if action_number == 1:
                add_contact(DEFAULT_DATABASE_NAME)

            elif action_number == 2:
                find_contact(DEFAULT_DATABASE_NAME) 

            elif action_number == 3:
                edit_contact(DEFAULT_DATABASE_NAME)

            elif action_number == 4:
                delete_contact(DEFAULT_DATABASE_NAME)
            
            elif action_number == 5:
                list_contacts(DEFAULT_DATABASE_NAME)

            elif action_number == 6:
                print("Дякуємо за використання! Дані збережено. Вихід.")
                break # Вихід з циклу while True

        except (ValueError, TypeError) as e:
            # Обробка помилок валідації (невірний ввід)
            print(f"\n[!] Помилка вводу: {e}. Спробуйте ще раз.\n")
        except KeyboardInterrupt:
            # Обробка Ctrl+C для чистого виходу
            print('\nВихід... До побачення!')
            break
        except Exception as e:
            # Загальна обробка інших помилок
            print(f"\n[!] Сталася неочікувана помилка: {e}\n")