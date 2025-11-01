import json
import os

def delete_contact(db_name):
    """
    Знаходить контакт за номером телефону та видаляє його
    після підтвердження користувача.
    """
    try:
        with open(db_name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"[!] Помилка: Неможливо прочитати базу даних '{db_name}'.")
        return

    contacts = db.get('contacts', [])
    if not contacts:
        print("\n[i] Телефонна книга порожня. Немає чого видаляти.")
        return

    # --- Крок 1: Запитати номер ---
    number_to_delete = input("Введіть номер телефону для видалення: ").strip()

    if not number_to_delete:
        print("[!] Порожній запит. Видалення скасовано.")
        return

    # --- Крок 2: Знайти контакт ---
    contact_to_delete = None
    for contact in contacts:
        # .get() для безпечної перевірки
        if contact.get('phone_number') == number_to_delete:
            contact_to_delete = contact
            break # Знайшли, тож виходимо з циклу

    # --- Крок 3: Обробка результату ---
    if contact_to_delete:
        # Ми знайшли контакт
        name = contact_to_delete.get('name', 'N/A')
        city = contact_to_delete.get('city', 'N/A')
        
        print("\n--- Знайдено контакт ---")
        print(f"Ім'я:   {name}")
        print(f"Номер: {number_to_delete}")
        print(f"Місто: {city}")
        
        # --- Крок 4: Підтвердження ---
        confirm = input("\nВи впевнені, що хочете видалити цей контакт? (так/ні): ").strip().lower()
        
        if confirm == 'так':
            # --- Крок 5: Видалення і збереження ---
            db['contacts'].remove(contact_to_delete)
            
            try:
                with open(db_name, 'w', encoding='utf-8') as f:
                    json.dump(db, f, indent=4, ensure_ascii=False)
                print(f"\n[✓] Контакт '{name}' успішно видалено.")
            except IOError as e:
                print(f"[!] Помилка при збереженні файлу: {e}")
        else:
            print("\n[i] Видалення скасовано.")
            
    else:
        # Ми не знайшли контакт
        print(f"\n[!] Контакт з номером '{number_to_delete}' не знайдено.")


# --- Блок для тестування ---
if __name__ == '__main__':
    DEFAULT_DATABASE_NAME = 'phonebook.json'
    
    if not os.path.exists(DEFAULT_DATABASE_NAME):
        print(f"Файл {DEFAULT_DATABASE_NAME} не знайдено для тесту.")
    else:
        print("Тестування delete_contact()...")
        # Спочатку покажемо, що є
        from list_module import list_contacts
        print("--- Поточні контакти ---")
        list_contacts(DEFAULT_DATABASE_NAME)
        print("-------------------------")
        
        delete_contact(DEFAULT_DATABASE_NAME)
        
        print("\n--- Оновлені контакти ---")
        list_contacts(DEFAULT_DATABASE_NAME)