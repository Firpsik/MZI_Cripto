table = {
    'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ё': 5, 'ж': 6, 'з': 7,
    'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15,
    'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23,
    'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31
}

reverse_table = {v: k for k, v in table.items()}

def caesar_decipher(text, shift):
    encrypted_text = []
    for char in text:
        if char in table:
            shifted_code = (table[char] + shift) % 32
            encrypted_text.append(reverse_table[shifted_code])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

text = "извлитевлцьиезъвдъжязцлмвпввйкибъеяювйеъжязцзялмиецкъбевсзхжяалиыиг"
auth_composit = "александрпушкиневгенийонегин"
k = 6
en_text = caesar_decipher(auth_composit, k)
print(f"Зашифрованный текст: {text}")
print(f"Расшифрованный текст: {caesar_decipher(text, k)}")
print(f"Автор и произведение: {auth_composit}")
print(f"Зашифрованный автор и произведение: {caesar_decipher(auth_composit, k)}")

while True:
    print("\nВыберите действие:")
    print("1. Расшифровать текст")
    print("2. Зашифровать текст")
    print("q. Выйти")
    choice = input("Ваш выбор: ")

    if choice == "q":
        break
    if choice != "1" and choice != "2":
        print("Ошибка: неверный ввод. Выберите 1, 2 или 'q'.")
        continue

    text_to_cipher = input("Введите текст для обработки: ").lower()
    k = input("Введите сдвиг (k): ")

    if not k.isdigit():
        print("Ошибка: сдвиг должен быть числом.")
        continue

    k = int(k)
    
    if choice == "1":
        result = caesar_decipher(text_to_cipher, k)
        print(f"Расшифрованный текст: {result}")
    elif choice == "2":
        result = caesar_decipher(text_to_cipher, -1*k)
        print(f"Зашифрованный текст: {result}")
