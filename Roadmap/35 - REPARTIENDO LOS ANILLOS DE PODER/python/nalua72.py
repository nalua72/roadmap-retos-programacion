"""
/*
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */
"""


def is_prime(n: int) -> bool:
    """
    Returns if a number is prime

    :param n: Description
    :type n: int
    :return: Description
    :rtype: bool
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_distributions(total_rings: int) -> list[tuple[int, int, int]]:
    """
    Returns valid distributions as tuples:
    (men, elves, dwarves)
    """
    valid_distributions = []

    for men in range(2, total_rings + 1, 2):  # pares
        for elves in range(1, total_rings + 1, 2):  # impares
            dwarves = total_rings - men - elves
            if dwarves > 0 and is_prime(dwarves):
                valid_distributions.append((men, elves, dwarves))

    return valid_distributions


def show_distributions(distributions: list[tuple[int, int, int]]) -> None:
    """Shows all possible distributions of the rings"""

    if not distributions:
        print("No existe posibilidad de reparto")
        return

    print("\nPosibles repartos de los anillos:\n")

    for ind, (men, elves, dwarves) in enumerate(distributions, start=1):
        print(
            f"{ind}.- Sauron recibe 1 anillo. Los Hombres reciben {men} anillos. Los Elfos reciben {elves} anillos. Los Enanos reciben {dwarves} anillos")


def main():
    SAURON = 1

    while True:
        try:
            total_rings = int(
                input("Introduce el número de anillos a repartir: "))
            if total_rings <= SAURON:
                raise ValueError
            break
        except ValueError:
            print("Introduce un número entero mayor que 1")

    rings_to_share = total_rings - SAURON
    distributions = find_distributions(rings_to_share)
    show_distributions(distributions)


if __name__ == "__main__":
    main()
