table = {
    'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ё': 5, 'ж': 6, 'з': 7,
    'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15,
    'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23,
    'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31
}

reverse_table = {v: k for k, v in table.items()}

def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char in table:
            shifted_code = (table[char] + shift) % 32
            encrypted_text.append(reverse_table[shifted_code])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

text = input("Введите строку для шифрования: ").lower()

while True:
    k = input("Введите сдвиг (k): (q для выхода) ")
    if k == "q":
        break
    if k.isdigit():
        k = int(k)
        result = caesar_cipher(text, k)
        print(f"Зашифрованная строка: {result}")
    else:
        print("Ошибка: сдвиг должен быть числом или 'q' для выхода.")
