import os
import json

# Change that if you don't want to enter data manually
__DEVELOPMENT_MODE__ = os.environ.get('DEVELOPMENT_MODE', False)


def add_contact(db_name):
    """Get user input, and create a contact if absent"""
    if __DEVELOPMENT_MODE__:
        phone_number = "123"
        name = "User1"
        city = "City1"
    else:
        phone_number = input('Введіть номер телефону (лише цифри): ')
        name = input('Введіть ім\'я: ')
        city = input('Введіть місто: ')

    # Assume only numbers are in phone_number
    clean_number = phone_number.strip()

    # Construct a line to be written into database
    datum = {'phone_number': clean_number, 'name': name, 'city': city}

    # open database and parse it into json
    try:
        with open(db_name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Якщо файл не знайдено або він порожній/пошкоджений,
        # створюємо нову структуру
        db = {'contacts': []}


    # append item to the contacts list
    db['contacts'].append(datum)

    # write `db` dictionary to the json database
    with open(db_name, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
    
    print(f"\n[+] Контакт {name} ({clean_number}) успішно додано.")


if __name__ == '__main__':
    # Це для тестування самого модуля, 
    # визначимо DEFAULT_DATABASE_NAME тут тимчасово
    DEFAULT_DATABASE_NAME = 'phonebook.json'
    
    # Переконаємось, що файл існує (той самий код, що в phonebook.py)
    if not os.path.exists(DEFAULT_DATABASE_NAME):
        empty_db = {'contacts': []}
        json.dump(empty_db, open(DEFAULT_DATABASE_NAME, 'w'))

    add_contact(DEFAULT_DATABASE_NAME)