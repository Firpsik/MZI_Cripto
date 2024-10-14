import dicts as d
import os

def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char in d.table:
            shifted_code = (d.table[char] - shift) % 32
            encrypted_text.append(d.reverse_table[shifted_code])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def open_file(name):
    with open(f"{name}.txt", encoding="utf-8") as init_f:
        lines = init_f.readlines()
        return lines

def save_file(content, name, m="a"):
    with open(f"{name}.txt", mode=m, encoding="utf-8") as file:
        file.write(content + "\n")

def error_message(error_name):
    os.system('cls')
    print(f"Ошибка: {error_name}")

def check_k(k):
    if not k.isdigit():
        error_message("сдвиг должен быть числом.")
    else:
        k = int(k)