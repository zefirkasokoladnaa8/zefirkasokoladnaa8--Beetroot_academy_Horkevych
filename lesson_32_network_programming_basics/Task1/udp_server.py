# --- UDP SERVER (СЕРВЕР) ---
# Запускаємо цей файл ПЕРШИМ.

import socket

HOST = '127.0.0.1'
PORT = 65432

print(f"UDP Server listening on {HOST}:{PORT}...")

# SOCK_DGRAM означає протокол UDP (Datagram)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Мы повинні "зайняти порт, щоб нам могли писати 
    s.bind((HOST, PORT))
    
    while True:
        # recvfrom повертає дані і адресу відправника
        # В UDP немає постійного з'єднання (conn), тому адреса приходить з кожним пакетом
        data, addr = s.recvfrom(1024)
        
        print(f"Received message from {addr}: {data}")
        
        if not data:
            break
            
        # Відправляємо відповідь конкретно цьому адресату (addr)
        # s.sendto(що відправити, кому відправити)
        response = data.upper()
        s.sendto(response, addr)