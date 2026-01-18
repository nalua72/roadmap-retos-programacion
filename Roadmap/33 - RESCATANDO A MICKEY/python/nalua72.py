from enum import Enum

"""
    * EJERCICIO:
    * ¡Disney ha presentado un montón de novedades en su D23!
    * Pero... ¿Dónde está Mickey?
    * Mickey Mouse ha quedado atrapado en un laberinto mágico
    * creado por Maléfica.
    * Desarrolla un programa para ayudarlo a escapar.
    * Requisitos:
    * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
    * 2. Los valores de las celdas serán:
    * - ⬜️ Vacío
    * - ⬛️ Obstáculo
    * - 🐭 Mickey
    * - 🚪 Salida
    * Acciones:
    * 1. Crea una matriz que represente el laberinto(no hace falta
    * que se genere de manera automática).
    * 2. Interactúa con el usuario por consola para preguntarle hacia
    * donde se tiene que desplazar(arriba, abajo, izquierda o derecha).
    * 3. Muestra la actualización del laberinto tras cada desplazamiento.
    * 4. Valida todos los movimientos, teniendo en cuenta los límites
    * del laberinto y los obstáculos. Notifica al usuario.
    * 5. Finaliza el programa cuando Mickey llegue a la salida.
"""


class Element(Enum):
    """Enumeramos los posibles valores del laberinto"""
    BLANK = "⬜️"
    OBSTACLE = "⬛️"
    MICKEY = "🐭"
    EXIT = "🚪"


class Maze:

    def __init__(self) -> None:
        self.maze_grid: list[list[Element]] = []
        self.mickey_position: list[int] = [0, 0]

        self.maze_grid = [
            [Element.MICKEY, Element.OBSTACLE, Element.BLANK,
                Element.BLANK, Element.BLANK, Element.BLANK],
            [Element.BLANK, Element.BLANK, Element.BLANK,
                Element.OBSTACLE, Element.OBSTACLE, Element.BLANK],
            [Element.BLANK, Element.BLANK, Element.OBSTACLE,
                Element.OBSTACLE, Element.BLANK, Element.BLANK],
            [Element.BLANK, Element.OBSTACLE, Element.OBSTACLE,
                Element.BLANK, Element.BLANK, Element.OBSTACLE],
            [Element.BLANK, Element.BLANK, Element.OBSTACLE,
                Element.OBSTACLE, Element.BLANK, Element.BLANK],
            [Element.BLANK, Element.BLANK, Element.OBSTACLE,
                Element.BLANK, Element.OBSTACLE, Element.EXIT]
        ]

        self.size = len(self.maze_grid)

    def maze_draw(self):
        for row in self.maze_grid:
            print(" ".join(cell.value for cell in row))

    def calculate_position(self, position: list[int], movement: str) -> list[int] | None:
        """Calculates the next position. Returns None if position is out of the grid"""
        row, col = position

        match movement:
            case "L":
                col -= 1
            case "R":
                col += 1
            case "U":
                row -= 1
            case "D":
                row += 1

        if not (0 <= row < self.size and 0 <= col < self.size):
            return None

        return [row, col]


class InputHandler:

    def get_user_directions(self) -> str:
        direction: str = ""

        while direction not in ("L", "R", "U", "D"):
            direction = input(
                "Por favor, introduce desplazamiento (L=Izquierda, R=Derecha, U=Arriba, D=Abajo): ")

        return direction


class MazeRunner:

    def maze_running(self, maze: Maze, input_user: InputHandler) -> bool:
        while True:
            user_option = input_user.get_user_directions()
            new_position = maze.calculate_position(
                maze.mickey_position.copy(), user_option)

            if new_position is None:
                print("Opción Invalida. Te sales del laberinto")
                continue

            if maze.maze_grid[new_position[0]][new_position[1]] == Element.OBSTACLE:
                print("Opción Invalida. Hay un obstáculo")
                continue

            if maze.maze_grid[new_position[0]][new_position[1]] == Element.EXIT:
                maze.maze_grid[maze.mickey_position[0]
                               ][maze.mickey_position[1]] = Element.BLANK
                maze.maze_grid[new_position[0]
                               ][new_position[1]] = Element.MICKEY
                maze.mickey_position = new_position
                maze.maze_draw()
                return True

            maze.maze_grid[maze.mickey_position[0]
                           ][maze.mickey_position[1]] = Element.BLANK
            maze.maze_grid[new_position[0]][new_position[1]] = Element.MICKEY

            maze.mickey_position = new_position

            maze.maze_draw()


def main():
    laberinto = Maze()
    # laberinto.initialize_maze()
    laberinto.maze_draw()

    user_handler = InputHandler()
    maze = MazeRunner()

    if maze.maze_running(laberinto, user_handler):
        print("Laberinto resuelto")


if __name__ == "__main__":
    main()
