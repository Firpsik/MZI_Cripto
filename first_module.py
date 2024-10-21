from dicts import table, reverse_table
import os

def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char in table:
            shifted_code = (table[char] - shift) % 32
            encrypted_text.append(reverse_table[shifted_code])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def var_input():
    while True:
        f_or_t = input("Введите 'ф', если текст из файла, или 'т' для ввода текста вручную: ").lower()
        if f_or_t == "ф":
            file_name = input("Введите название файла: ")
            try:
                user_file = open_file(file_name)
                text = user_file[0].strip()
                k = user_file[1].strip()
                if not k.isdigit():
                    error_message("Сдвиг должен быть числом.")
                    continue
                k = int(k)
                return text, k
            except OSError:
                error_message("Файла не существует. Попробуйте снова.")
        elif f_or_t == "т":
            text = input("Введите текст для обработки: ").lower()
            k = input("Введите сдвиг (k): ")
            if not k.isdigit():
                error_message("Сдвиг должен быть числом.")
                continue
            k = int(k)
            return text, k
        else:
            error_message("Неверный ввод. Выберите 'ф' или 'т'.")

def open_file(name):
    with open(f"txt/{name}.txt", encoding="utf-8") as init_f:
        lines = init_f.readlines()
        return lines

def save_file(content, name, m="a"):
    with open(f"txt/{name}.txt", mode=m, encoding="utf-8") as file:
        file.write(content + "\n")

def error_message(error_name):
    os.system('cls')
    print(f"Ошибка: {error_name}")

def check_k(k):
    if not k.isdigit():
        error_message("сдвиг должен быть числом.")
    else:
        k = int(k)