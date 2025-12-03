# --- UDP CAESAR CLIENT  ---

import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65433

print("--- Шифрувальник Цезаря (UDP) ---")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        # Запитуємо у користувача дані
        print("\nВведіть повідомлення (або 'q' для виходу):")
        msg = input("> ").strip()
        
        if msg.lower() == 'q':
            break
            
        print("Введіть ключ шифрування (число, наприклад 3):")
        key = input("> ").strip()
        
        # Формуємо пакет за нашим протоколом: "КЛЮЧ:ПОВІДОМЛЕННЯ"
        packet = f"{key}:{msg}"
        
        # Відправляємо серверу (кодуємо в байти)
        s.sendto(packet.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
        
        # Чекаємо на відповідь
        try:
            # Ставимо тайм-аут 2 секунди
            s.settimeout(2)
            data, server = s.recvfrom(1024)
            print(f"Відповідь сервера: {data.decode('utf-8')}")
        except socket.timeout:
            print("Сервер мовчить (або пакет втрачено)...")