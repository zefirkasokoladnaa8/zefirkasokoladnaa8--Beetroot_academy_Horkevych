import json
import os

def edit_contact(db_name):
    """
    Знаходить контакт за номером телефону та дозволяє оновити 
    одне з його полів (ім'я, номер або місто).
    """
    try:
        with open(db_name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"[!] Помилка: Неможливо прочитати базу даних '{db_name}'.")
        return

    contacts = db.get('contacts', [])
    if not contacts:
        print("\n[i] Телефонна книга порожня. Немає чого редагувати.")
        return

    # --- Крок 1: Запитати номер ---
    number_to_edit = input("Введіть номер телефону для редагування: ").strip()

    if not number_to_edit:
        print("[!] Порожній запит. Редагування скасовано.")
        return

    # --- Крок 2: Знайти контакт ---
    # Нам потрібен не просто контакт, а його індекс (позиція) у списку,
    # щоб ми могли його оновити.
    found_contact = None
    contact_index = -1 # -1 означає "не знайдено"

    for i, contact in enumerate(contacts):
        if contact.get('phone_number') == number_to_edit:
            found_contact = contact
            contact_index = i # Зберігаємо індекс (позицію)
            break

    # --- Крок 3: Обробка результату ---
    if found_contact:
        # Ми знайшли контакт
        print("\n--- Знайдено контакт ---")
        print(f"1. Ім'я:   {found_contact.get('name', 'N/A')}")
        print(f"2. Номер: {found_contact.get('phone_number', 'N/A')}")
        print(f"3. Місто: {found_contact.get('city', 'N/A')}")
        
        # --- Крок 4: Вкладене меню редагування ---
        choice = input("\nЯке поле ви хочете оновити (1-3)? (або 'ні' для скасування): ").strip().lower()

        if choice == '1':
            field_key = 'name'
            field_name = "ім'я"
        elif choice == '2':
            field_key = 'phone_number'
            field_name = "номер"
        elif choice == '3':
            field_key = 'city'
            field_name = "місто"
        else:
            print("\n[i] Редагування скасовано.")
            return

        # --- Крок 5: Отримання нового значення ---
        new_value = input(f"Введіть нове значення для '{field_name}': ").strip()
        
        if not new_value:
             print("[!] Порожнє значення. Редагування скасовано.")
             return

        # --- Крок 6: Оновлення і збереження ---
        # Оновлюємо словник прямо у списку
        db['contacts'][contact_index][field_key] = new_value
        
        try:
            with open(db_name, 'w', encoding='utf-8') as f:
                json.dump(db, f, indent=4, ensure_ascii=False)
            print(f"\n[✓] Контакт успішно оновлено.")
        except IOError as e:
            print(f"[!] Помилка при збереженні файлу: {e}")
            
    else:
        # Ми не знайшли контакт
        print(f"\n[!] Контакт з номером '{number_to_edit}' не знайдено.")


# --- Блок для тестування ---
if __name__ == '__main__':
    DEFAULT_DATABASE_NAME = 'phonebook.json'
    
    if not os.path.exists(DEFAULT_DATABASE_NAME):
        print(f"Файл {DEFAULT_DATABASE_NAME} не знайдено для тесту.")
    else:
        print("Тестування edit_contact()...")
        # Спочатку покажемо, що є
        from list_module import list_contacts
        print("--- Поточні контакти ---")
        list_contacts(DEFAULT_DATABASE_NAME)
        print("-------------------------")
        
        edit_contact(DEFAULT_DATABASE_NAME)
        
        print("\n--- Оновлені контакти ---")
        list_contacts(DEFAULT_DATABASE_NAME)