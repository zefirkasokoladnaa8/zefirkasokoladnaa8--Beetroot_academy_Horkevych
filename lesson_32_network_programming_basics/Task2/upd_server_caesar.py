# --- UDP CAESAR SERVER ---
# Сервер, який шифрує отримані повідомлення шифром Цезаря.

import socket

HOST = '127.0.0.1'
PORT = 65433  # Використовуємо порт 65433

def caesar_cipher(text, shift):
    """
    Шифрує текст методом Цезаря зі зсувом shift.
    Підтримує базову кирилицю та латиницю.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Визначаємо межі алфавіту (для збереження регістру)
            if 'А' <= char <= 'Я' or 'а' <= char <= 'я':
                # Кирилиця
                start = ord('А') if char.isupper() else ord('а')
                alphabet_len = 32
            else:
                # Латиниця
                start = ord('A') if char.isupper() else ord('a')
                alphabet_len = 26
            
            # Формула зсуву: (код_символу - початок + зсув) % довжина + початок
            code = ord(char) - start
            new_code = (code + shift) % alphabet_len
            result += chr(start + new_code)
        else:
            # Розділові знаки та цифри не змінюємо
            result += char
    return result

print(f"Caesar Server слухає на {HOST}:{PORT}...")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    
    while True:
        try:
            # Отримуємо дані (максимум 1024 байти)
            data, addr = s.recvfrom(1024)
            decoded_data = data.decode('utf-8')
            
            print(f"Отримано від {addr}: {decoded_data}")
            
            # ПАРСИНГ: Очікуємо формат "КЛЮЧ:ПОВІДОМЛЕННЯ"
            if ':' in decoded_data:
                # Розділяємо тільки по першому двокрапці
                shift_str, message = decoded_data.split(':', 1)
                
                # Перевіряємо, чи є ключ числом (також підтримуємо від'ємні числа)
                if shift_str.isdigit() or (shift_str.startswith('-') and shift_str[1:].isdigit()):
                    shift = int(shift_str)
                    
                    # Шифруємо
                    encrypted_msg = caesar_cipher(message, shift)
                    
                    # Відправляємо назад
                    response = f"Зашифровано: {encrypted_msg}"
                    s.sendto(response.encode('utf-8'), addr)
                else:
                    error = "ПОМИЛКА: Ключ має бути цілим числом (наприклад, 3:Привіт)"
                    s.sendto(error.encode('utf-8'), addr)
            else:
                error = "ПОМИЛКА: Невірний формат. Використовуйте КЛЮЧ:ПОВІДОМЛЕННЯ"
                s.sendto(error.encode('utf-8'), addr)
                
        except Exception as e:
            print(f"Помилка: {e}")