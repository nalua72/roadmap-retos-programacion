"""
/*
 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 *
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 *
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 *
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 *
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).
 */
"""
import random


class ChristmasTree:

    def __init__(self, hight: int):
        self.hight = hight
        self.width = hight * 2 - 1
        self.base_tree: list[list[str]] = []
        self.tree_decorations: list[list[str]] = []
        self.star_on: bool = False
        self.visible_positions: list[tuple[int]] = []
        self.balls_position: list[tuple[int]] = []
        self.lights_position: list[tuple[int]] = []

        self.generate_base_tree()
        self.generate_tree_decorations()

    def print_christams_tree(self):
        """Prints the tree to the screen"""
        for row in range(self.hight + 2):
            line_to_print = []
            for column in range(self.width):
                if self.tree_decorations[row][column] == " ":
                    line_to_print.append(self.base_tree[row][column])
                else:
                    line_to_print.append(self.tree_decorations[row][column])

            print("".join(line_to_print))

    def add_star(self):
        """Adds the star to the tree"""
        if not self.star_on:
            self.tree_decorations[0][self.width // 2] = "@"
            self.star_on = True

    def remove_star(self):
        """Removes the star from the tree"""
        if self.star_on:
            self.tree_decorations[0][self.width // 2] = " "
            self.star_on = False

    def add_balls(self):
        """Adds the balls to the tree"""
        if len(self.visible_positions) < 2:
            print("No hay sitios disponibles para las bolas")
            return
        free_positions = [
            pos for pos in self.visible_positions
            if pos not in self.balls_position and pos not in self.lights_position
        ]

        ball1, ball2 = random.sample(free_positions, 2)

        self.tree_decorations[ball1[0]][ball1[1]] = "o"
        self.tree_decorations[ball2[0]][ball2[1]] = "o"

        self.balls_position.append(ball1)
        self.balls_position.append(ball2)

    def remove_balls(self):
        """Removes the balls from the tree"""
        if len(self.balls_position) < 2:
            print("No hay bolas que quitar")
            return

        ball1, ball2 = random.sample(self.balls_position, 2)

        self.tree_decorations[ball1[0]][ball1[1]] = " "
        self.tree_decorations[ball2[0]][ball2[1]] = " "

        self.balls_position.remove(ball1)
        self.balls_position.remove(ball2)

    def add_lights(self):
        """Adds the lights to the tree"""
        if len(self.visible_positions) < 3:
            print("No hay sitios disponibles para las luces")
            return

        free_positions = [
            pos for pos in self.visible_positions
            if pos not in self.balls_position and pos not in self.lights_position
        ]

        light1, light2, light3 = random.sample(free_positions, 3)

        self.tree_decorations[light1[0]][light1[1]] = "+"
        self.tree_decorations[light2[0]][light2[1]] = "+"
        self.tree_decorations[light3[0]][light3[1]] = "+"

        self.lights_position.append(light1)
        self.lights_position.append(light2)
        self.lights_position.append(light3)

    def remove_lights(self):
        """Removes the lights from the tree"""
        if len(self.lights_position) < 3:
            print("No hay luces que quitar")
            return

        light1, light2, light3 = random.sample(self.lights_position, 3)

        self.tree_decorations[light1[0]][light1[1]] = " "
        self.tree_decorations[light2[0]][light2[1]] = " "
        self.tree_decorations[light3[0]][light3[1]] = " "

        self.lights_position.remove(light1)
        self.lights_position.remove(light2)
        self.lights_position.remove(light3)

    def turn_lights_on(self):
        """Turns the lights off"""
        if len(self.lights_position) == 0:
            print("No hay luces en el árbol")
            return

        for light in self.lights_position:
            self.tree_decorations[light[0]][light[1]] = "+"

    def turn_lights_off(self):
        """Turns the lights off"""
        if len(self.lights_position) == 0:
            print("No hay luces en el árbol")
            return

        for light in self.lights_position:
            self.tree_decorations[light[0]][light[1]] = "*"

    def generate_base_tree(self):
        """Generates the christams tree according to the hight provided by the user"""
        num_visible_pos = 1

        for i in range(self.hight):
            row = []
            num_non_visible_pos = self.width - num_visible_pos

            for _ in range(num_non_visible_pos // 2):
                row.append(" ")
            for j in range(num_visible_pos):
                row.append("*")
                self.visible_positions.append(
                    (i, num_non_visible_pos // 2 + j))
            for _ in range(num_non_visible_pos // 2):
                row.append(" ")

            num_visible_pos += 2

            self.base_tree.append(row)

        # Special case. Star position
        self.visible_positions.remove((0, self.width // 2))

        num_non_visible_pos = self.width - 3
        row = []
        for _ in range(num_non_visible_pos // 2):
            row.append(" ")
        for _ in range(3):
            row.append("|")
        for _ in range(num_non_visible_pos // 2):
            row.append(" ")

        self.base_tree.append(row)
        self.base_tree.append(row)

    def generate_tree_decorations(self):
        """Generates a full empty matrix like the tree where decorations will be added"""
        for _ in range(self.hight + 2):
            row = []
            for _ in range(self.width):
                row.append(" ")

            self.tree_decorations.append(row)


def menu_interactivo():
    """Manages user options"""
    while True:
        try:
            altura = int(input("Introduce la altura del árbol (mínimo 3): "))
            if altura < 3:
                print("La altura debe ser al menos 3.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    arbol = ChristmasTree(altura)

    while True:
        print("\nÁrbol actual:")
        arbol.print_christams_tree()

        print("\nOpciones:")
        print("1 - Añadir estrella")
        print("2 - Quitar estrella")
        print("3 - Añadir bolas")
        print("4 - Quitar bolas")
        print("5 - Añadir luces")
        print("6 - Quitar luces")
        print("7 - Encender luces")
        print("8 - Apagar luces")
        print("0 - Salir")

        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "1":
                arbol.add_star()
            case "2":
                arbol.remove_star()
            case "3":
                arbol.add_balls()
            case "4":
                arbol.remove_balls()
            case "5":
                arbol.add_lights()
            case "6":
                arbol.remove_lights()
            case "7":
                arbol.turn_lights_on()
            case "8":
                arbol.turn_lights_off()
            case "0":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")


def main():
    menu_interactivo()


if __name__ == "__main__":
    main()
