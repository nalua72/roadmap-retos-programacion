"""
/*
 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 *
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario selecciona qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
 */
"""


def print_calendar(open_days):
    """ Prints a 4x3 calendar"""

    border = " ".join(["****"] * 6)

    for x in range(4):

        # Superior row
        print(border)

        # Central row
        row = []
        for y in range(6):
            day = x * 6 + y + 1
            if day in open_days:
                row.append("****")
            else:
                row.append(f"*{day:02}*")
        print(" ".join(row))

        # Inferior row
        print(border)


def user_day_choice() -> int:
    """ Gets the user day of choice"""
    while True:
        try:
            day = int(
                input("Por favor, dime un día del 1 al 24 (pulsa 0 para salir): "))
            if 0 <= day < 25:
                return day
        except ValueError:
            print("Debes seleccionar un número entre 0 y 24")


def main():
    """ Controls the flow of the app"""
    dias_abiertos = set()

    print_calendar(dias_abiertos)

    while True:
        dia = user_day_choice()

        if dia == 0:
            break

        if dia in dias_abiertos:
            print(f"El día {dia} ya fue abierto")
        else:
            print(f"Enhorabuena. Aquí tienes tu premio")
            dias_abiertos.add(dia)
            print_calendar(dias_abiertos)


if __name__ == "__main__":
    main()
