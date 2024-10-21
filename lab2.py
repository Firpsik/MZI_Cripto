import os
from dicts import table
from second_module import var_input, mod_inverse, solve_mod_equation, solve_mod_system, frequency_analysis, affine_decrypt, brute_force_affine

alphabet = "".join(table)
alphabet = alphabet.replace("ё","")
m = len(alphabet)

menu = """
    1. Найти обратный элемент по модулю
    2. Решить сравнение a * x ≡ b (mod m)
    3. Решить систему сравнений
    4. Выполнить частотный анализ текста
    5. Расшифровать текст с помощью известного ключа
    6. Выполнить перебор ключей для расшифровки
    q. Выйти
"""

while True:
    print("\nВыберите действие:")
    print(menu)
    choice = input("Введите номер действия: ")

    if choice == "1":
        os.system('CLS')
        print("Поиск обратного элемента по модулю\n")
        a = int(input("Введите элемент a: "))
        mod = int(input("Введите модуль m: "))
        try:
            inv = mod_inverse(a, mod)
            print(f'Обратный элемент: {inv}')
        except ValueError as e:
            print(e)

    elif choice == "2":
        os.system('CLS')
        print("Решение сравнения a * x ≡ b (mod m)\n")
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        mod = int(input("Введите модуль m: "))
        try:
            result = solve_mod_equation(a, b, mod)
            print(f"Решение уравнения: {result}")
        except ValueError as e:
            print(e)

    elif choice == "3":
        os.system('CLS')
        print("Решение системы сравнений\n")
        a1 = int(input("Введите a1: "))
        b1 = int(input("Введите b1: "))
        a2 = int(input("Введите a2: "))
        b2 = int(input("Введите b2: "))
        mod = int(input("Введите модуль m: "))
        try:
            solutions = solve_mod_system(a1, b1, a2, b2, mod)
            print(f"Решения системы сравнений: {solutions}")
        except ValueError as e:
            print(e)

    elif choice == "4":
        os.system('CLS')
        print("Выполнение частотного анализа текста\n")
        cipher_text = var_input()
        most_common = frequency_analysis(cipher_text)
        print(f'Две наиболее частые буквы: {most_common}')

    elif choice == "5":
        os.system('CLS')
        print("Расшифровка текста с помощью известного ключа\n")
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        cipher_text = var_input()
        try:
            plaintext = affine_decrypt(cipher_text, a, b, m)
            print(f'Расшифрованный текст: {plaintext}')
        except ValueError as e:
            print(e)

    elif choice == "6":
        os.system('CLS')
        print("Выполнение полного перебора ключей для расшифровки\n")
        cipher_text = var_input()
        brute_force_affine(cipher_text)
        print("Перебор завершен. Результаты сохранены в файл 'decryption_result.txt'.")

    elif choice == "q":
        os.system('CLS')
        print("Выход из программы.")
        break
    
    else:
        os.system('CLS')
        print("Неверный ввод. Пожалуйста, попробуйте снова.")
