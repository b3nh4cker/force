import itertools
import random
import string

def generate_passwords(base_words, length, count, use_symbols=True, use_numbers=True):
    characters = string.ascii_letters
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    passwords = set()

    # Generar variaciones de las palabras base con números y símbolos
    for word in base_words:
        for _ in range(count // len(base_words)):
            # Añadir números y símbolos al final de la palabra
            password = word + ''.join(random.choices(characters, k=length - len(word)))
            passwords.add(password)

            # Añadir números y símbolos al principio de la palabra
            password = ''.join(random.choices(characters, k=length - len(word))) + word
            passwords.add(password)

            # Insertar números y símbolos en medio de la palabra
            for i in range(1, len(word)):
                password = word[:i] + ''.join(random.choices(characters, k=1)) + word[i:]
                passwords.add(password)

    # Generar contraseñas aleatorias adicionales si es necesario
    while len(passwords) < count:
        password = ''.join(random.choices(characters, k=length))
        passwords.add(password)

    return list(passwords)[:count]

def main():
    base_words = input("Introduce palabras base separadas por comas: ").split(',')
    length = int(input("Introduce la longitud de las contraseñas (8-16): "))
    count = int(input("Introduce la cantidad de contraseñas a generar: "))
    use_symbols = input("¿Incluir símbolos? (s/n): ").lower() == 's'
    use_numbers = input("¿Incluir números? (s/n): ").lower() == 's'

    if length < 8 or length > 16:
        print("La longitud de las contraseñas debe estar entre 8 y 16 caracteres.")
        return

    passwords = generate_passwords(base_words, length, count, use_symbols, use_numbers)

    with open('diccionario.txt', 'w') as file:
        for password in passwords:
            file.write(password + '\n')

    print(f"Se han generado {len(passwords)} contraseñas y se han guardado en 'diccionario.txt'.")

if __name__ == "__main__":
    main()