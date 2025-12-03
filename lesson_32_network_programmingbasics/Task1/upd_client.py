# --- UDP CLIENT (КЛІЕНТ) ---
# Запускємо другим.

import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

print("UDP Client started...")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = b"Hello, UDP World!"
    
    # В UDP мы не робимо connect(). Просто кидаємо пакет в сторону сервера.
    # s.sendto(дані, (IP_адреса, Порт))
    print(f"Sending to {SERVER_HOST}:{SERVER_PORT} -> {message}")
    s.sendto(message, (SERVER_HOST, SERVER_PORT))
    
    # Чекаємо відповідь (якщо віна прийде, UDP нічого не гарантує)
    try:
        # Ставимо тайм-аут 2 секунди. Если сервер не відповість, ми не будемо висети вічно.
        s.settimeout(2)
        data, server = s.recvfrom(1024)
        print(f"Received from server: {repr(data)}")
    except socket.timeout:
        print("REQUEST TIMED OUT: Сервер не відповів (або пакет загубився).")