import my_module as mod
import os

init_data = mod.open_file("init")
text = init_data[0].strip()
auth_composit = init_data[1].strip()
k = int(init_data[2].strip())

en_text = mod.caesar_cipher(auth_composit, k)

init_output = (
    f"ШИФР-ТЕКСТ (ШТ): {text}\n"
    f"РАСШИФРОВАННЫЙ ТЕКСТ (ОТ): {mod.caesar_cipher(text, k)}\n"
    f"КЛЮЧ: {k}\n"
    f"АВТОР И ПРОИЗВЕДЕНИЕ (ОТ): {auth_composit}\n"
    f"ЗАШИФРОВАННЫЕ ФАМИЛИЯ И НАЗВАНИЕ (ШТ): {mod.caesar_cipher(auth_composit, -k)}"
)
mod.save_file(init_output, "processing", "w")
print(f"Начальные данные сохранены в файл 'processing.txt'.")

for k in range(1,32):
    mod.save_file(f"k={k}: {mod.caesar_cipher(text, k)}", "full")
print(f"Полный перебор сохранён в файл 'full.txt'.")

while True:
    print("\nВыберите действие:")
    print("1. Расшифровать текст")
    print("2. Зашифровать текст")
    print("q. Выйти")
    choice = input("Ваш выбор: ")

    if choice == "q":
        break
    if choice != "1" and choice != "2":
        os.system('cls')
        print("неверный ввод. Выберите 1, 2 или 'q'.")
        continue

    f_or_t = input("Введите 'ф', если текст из файла, или 'т' для ввода текста вручную: ").lower()
    if f_or_t != "ф" and f_or_t != "т":
        mod.error_message("неверный ввод. Выберите 'ф' или 'т'.")
        continue

    if f_or_t == "ф":
        file_name = input("Введите название файла: ")
        try:
            user_file = mod.open_file(file_name)
            text_to_cipher = user_file[0].strip()
            k = user_file[1].strip()
            if not k.isdigit():
                mod.error_message("сдвиг должен быть числом.")
                continue
            k = int(k)
        except OSError:
            mod.error_message("файла не существует.")
            continue

    if f_or_t == "т":
        text_to_cipher = input("Введите текст для обработки: ").lower()
        k = input("Введите сдвиг (k): ")
        if not k.isdigit():
            mod.error_message("сдвиг должен быть числом.")
            continue
        k = int(k)

    if choice == "1":
        result = mod.caesar_cipher(text_to_cipher, k)
    elif choice == "2":
        result = mod.caesar_cipher(text_to_cipher, -1 * k)

    print(result)

    save_choice = input("Хотите сохранить результат в файл? (да/нет): ").lower()
    if save_choice == "да":
        mod.save_file(result, "result")
        os.system('cls')
        print("Результат сохранен в файл 'result.txt'.")
    else:
        os.system('cls')
        print("Результат не был сохранен.")
