import json
import os

def list_contacts(db_name):
    """
    Завантажує та виводить на екран всі контакти з бази даних,
    відсортовані за ім'ям.
    """
    try:
        with open(db_name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"[!] Помилка: Неможливо прочитати базу даних '{db_name}'.")
        print("Спробуйте спочатку додати контакт.")
        return

    contacts = db.get('contacts', [])

    if not contacts:
        print("\n[i] Телефонна книга порожня.")
        return


    # Сортуємо список 'contacts' за ключем 'name', ігноруючи регістр
    # 'item.get('name', '')' - безпечно бере ім'я, 
    # або порожній рядок, якщо імені раптом немає
    try:
        sorted_contacts = sorted(contacts, key=lambda item: item.get('name', '').lower())
    except Exception as e:
        print(f"[!] Помилка сортування: {e}. Виводимо список як є.")
        sorted_contacts = contacts # Якщо сортування не вдалося, покажемо як є
    # -------------------------

    print(f"\n--- Всього контактів: {len(sorted_contacts)} ---")
    
    # Перебираємо відсортований список
    for i, contact in enumerate(sorted_contacts, start=1):
        name = contact.get('name', 'N/A')
        phone = contact.get('phone_number', 'N/A')
        city = contact.get('city', 'N/A')
        
        print(f"{i}. Ім'я:   {name}")
        print(f"   Номер: {phone}")
        print(f"   Місто: {city}")
        print("-" * 20)

# --- Блок для тестування ---
if __name__ == '__main__':
    DEFAULT_DATABASE_NAME = 'phonebook.json'
    
    if not os.path.exists(DEFAULT_DATABASE_NAME):
        print("Файл phonebook.json не знайдено.")
    else:
        print("Тестування list_contacts() з сортуванням...")
        list_contacts(DEFAULT_DATABASE_NAME)