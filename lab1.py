from first_module import caesar_cipher, var_input, error_message, open_file, save_file
import os

init_data = open_file("init")
text = init_data[0].strip()
auth_composit = init_data[1].strip()
k = int(init_data[2].strip())

en_text = caesar_cipher(auth_composit, k)

init_output = (
    f"ШИФР-ТЕКСТ (ШТ): {text}\n"
    f"РАСШИФРОВАННЫЙ ТЕКСТ (ОТ): {caesar_cipher(text, k)}\n"
    f"КЛЮЧ: {k}\n"
    f"АВТОР И ПРОИЗВЕДЕНИЕ (ОТ): {auth_composit}\n"
    f"ЗАШИФРОВАННЫЕ ФАМИЛИЯ И НАЗВАНИЕ (ШТ): {caesar_cipher(auth_composit, -k)}"
)
save_file(init_output, "processing", "w")
print(f"Начальные данные сохранены в файл 'processing.txt'.")

for k in range(1, 32):
    save_file(f"k={k}: {caesar_cipher(text, k)}", "full")
print(f"Полный перебор сохранён в файл 'full.txt'.")

menu = """
    1. Расшифровать текст
    2. Зашифровать текст
    q. Выйти
"""

while True:
    print("\nВыберите действие:")
    print(menu)
    choice = input("Ваш выбор: ")

    if choice == "q":
        os.system("CLS")
        print("Выход из программы.")
        break
    elif choice not in ("1", "2"):
        os.system("CLS")
        error_message("Неверный ввод. Выберите 1, 2 или 'q'.")
        continue
    text_to_cipher, k = var_input()

    if choice == "1":
        os.system("CLS")
        print("Расшифровка текста:\n")
        result = caesar_cipher(text_to_cipher, k)
    elif choice == "2":
        os.system("CLS")
        print("Шифровка текста:\n")
        result = caesar_cipher(text_to_cipher, -k)
    print(f"{result}\n")

    save_choice = input("Хотите сохранить результат в файл? (да/нет): ").lower()
    os.system("CLS")
    if save_choice == "да":
        save_file(result, "result")
        print("Результат сохранен в файл 'result.txt'.")
    else:
        print("Результат не был сохранен.")
