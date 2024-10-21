from first_module import error_message, open_file
from collections import Counter
from lab2 import alphabet, m

def affine_decrypt(ciphertext, a, b, m, alphabet=alphabet):
    a_inv = mod_inverse(a, m)
    plaintext = ''
    for char in ciphertext:
        if char.lower() in alphabet:
            y = alphabet.index(char.lower())
            x = (a_inv * (y - b)) % m
            decrypted_char = alphabet[x]
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def var_input():
    while True:
        f_or_t = input("Введите 'ф', если текст из файла, или 'т' для ввода текста вручную: ").lower()
        if f_or_t == "ф":
            while True:
                file_name = input("Введите название файла: ")
                try:
                    user_file = open_file(file_name)
                    cipher_text = user_file[0].strip().lower()
                    return cipher_text
                except OSError:
                    error_message("Файла не существует. Попробуйте снова.")
        elif f_or_t == "т":
            return input("Введите текст для обработки: ").lower()
        else:
            error_message("Неверный ввод. Выберите 'ф' или 'т'.")

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f'Нет обратного элемента для {a} по модулю {m}')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def solve_mod_equation(a, b, m):
    g, _, _ = extended_gcd(a, m)
    if b % g != 0:
        raise ValueError(f'Нет решений для уравнения {a}x ≡ {b} (mod {m})')
    a_ = a // g
    b_ = b // g
    m_ = m // g
    try:
        x0 = (mod_inverse(a_, m_) * b_) % m_
    except ValueError as e:
        raise ValueError(f'Не удалось найти частное решение: {e}')
    solutions = [(x0 + i * m_) % m for i in range(g)]
    return solutions

def solve_mod_system(a, b, c, d, m):
    delta_a = c - a
    delta_b = d - b
    try:
        x_solutions = solve_mod_equation(delta_a, delta_b, m)
    except ValueError as e:
        raise ValueError(f'Не удалось найти решения для x: {e}')
    y_solutions = [(x, (b - a * x) % m) for x in x_solutions]
    return y_solutions

def frequency_analysis(text):
    text = ''.join([c for c in text if c in alphabet])
    counter = Counter(text)
    most_common = counter.most_common(2)
    return most_common

def brute_force_affine(ciphertext):
    with open('txt/decryption_result.txt', 'w', encoding="UTF-8") as f:
        for a in range(1, m):
            if gcd(a, m) == 1:
                for b in range(m):
                    decrypted_text = affine_decrypt(ciphertext, a, b, m)
                    f.write(f'Ключи a={a}, b={b}: {decrypted_text}\n')