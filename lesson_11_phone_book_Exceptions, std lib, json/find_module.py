import json
import os

def print_contacts(contacts_list):
    """
    Допоміжна функція для красивого друку списку знайдених контактів.
    """
    if not contacts_list:
        print("\n[i] За вашим запитом нічого не знайдено.")
        return

    print(f"\n--- Знайдено контактів: {len(contacts_list)} ---")
    
    for i, contact in enumerate(contacts_list, start=1):
        name = contact.get('name', 'N/A')
        phone = contact.get('phone_number', 'N/A')
        city = contact.get('city', 'N/A')
        
        print(f"{i}. Ім'я:   {name}")
        print(f"   Номер: {phone}")
        print(f"   Місто: {city}")
        print("-" * 20)

def find_contact(db_name):
    """
    Головна функція пошуку.
    Шукає за ім'ям або номером телефону.
    """
    try:
        with open(db_name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"[!] Помилка: Неможливо прочитати базу даних '{db_name}'.")
        return

    contacts = db.get('contacts', [])
    if not contacts:
        print("\n[i] Телефонна книга порожня. Немає чого шукати.")
        return

    # --- Вкладене меню пошуку ---
    print("\nОберіть критерій пошуку:")
    print("1. Пошук за ім'ям")
    print("2. Пошук за номером телефону")
    
    choice = input("Ваш вибір (1-2): ").strip()
    
    search_term = input("Введіть запит для пошуку: ").strip().lower()
    
    if not search_term:
        print("[!] Порожній запит. Пошук скасовано.")
        return
        
    found_contacts = [] # Тут зберігатимемо результати

    if choice == '1':
        # --- Логіка пошуку за ім'ям ---
        search_key = 'name'
        for contact in contacts:
            # .get(search_key, '') - беремо ім'я, або порожній рядок
            # .lower() - переводимо в нижній регістр
            # 'in' - перевіряємо, чи наш запит є частиною імені
            if search_term in contact.get(search_key, '').lower():
                found_contacts.append(contact)
                
    elif choice == '2':
        # --- Логіка пошуку за номером ---
        search_key = 'phone_number'
        for contact in contacts:
            if search_term in contact.get(search_key, '').lower():
                found_contacts.append(contact)
                
    else:
        print("[!] Невірний вибір. Пошук скасовано.")
        return
        
    # Виводимо результати
    print_contacts(found_contacts)


# --- Блок для тестування ---
if __name__ == '__main__':
    DEFAULT_DATABASE_NAME = 'phonebook.json'
    
    if not os.path.exists(DEFAULT_DATABASE_NAME):
        print(f"Файл {DEFAULT_DATABASE_NAME} не знайдено для тесту.")
    else:
        print("Тестування find_contact()...")
        find_contact(DEFAULT_DATABASE_NAME)