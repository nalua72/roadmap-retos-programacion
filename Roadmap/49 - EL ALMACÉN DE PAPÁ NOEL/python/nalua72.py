"""
/*
 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
 */
"""
import random


def generate_code() -> str:
    """Generates a secret code"""

    alphabet = ["A", "B", "C", "1", "2", "3"]

    code = random.sample(alphabet, 4)

    return "".join(code)


def user_input() -> str:
    """Gets and validates the user input"""

    while True:
        user_code = input("Introduce un código de 4 caracteres (A-C 1-3): ")

        if len(user_code) != 4 or len(set(user_code)) != 4 or not check_character_in_alphabet(user_code):
            print("Código no válido")
        else:
            return user_code


def check_character_in_alphabet(string: str) -> bool:
    """Checks if the string is built with approved characters"""

    alphabet = ["A", "B", "C", "1", "2", "3"]

    for i, _ in enumerate(string):
        if string[i] not in alphabet:
            return False
    return True


def check_validity(code1: str, code2: str) -> bool:
    """Checks if the input code is the scret one"""

    correct_number = 0

    for pos in range(4):
        found = False
        for posc in range(4):
            if code1[pos] == code2[posc]:
                if pos == posc:
                    print("Correcto")
                    correct_number += 1
                else:
                    print("Presente")
                found = True
                break
        if not found:
            print("Incorrecto")

    if correct_number == 4:
        return True

    return False


def main():
    """Orchastrates the game"""
    number_of_attempts: int = 0

    secret_code = generate_code()

    while True:

        if number_of_attempts == 10:
            print("Lo lamento, has llegado al número máximo de intentos")
            break

        print(f"Intento {number_of_attempts + 1} de 10")

        user_attempt = user_input()

        print(f"User Attempt: {user_attempt}, Secret code: {secret_code}")

        if check_validity(user_attempt, secret_code):
            print("Enhorabuena has acertado el código")
            break

        number_of_attempts += 1


if __name__ == "__main__":
    main()
