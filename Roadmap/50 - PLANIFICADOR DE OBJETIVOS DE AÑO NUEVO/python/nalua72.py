"""
/*
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 *
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
 */
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Purpose:
    target: str
    amount: int
    units: str
    term: int


class PurposesManagement:
    """manages the purposes list"""

    def __init__(self) -> None:
        self.purposes_list: list[Purpose] = []

    def add_purpose(self, target: str, amount: int, units: str, term: int) -> None:
        """Add a purpose to a list of purposes"""
        if len(self.purposes_list) < 10:
            self.purposes_list.append(
                Purpose(target=target, amount=amount, units=units, term=term))
        else:
            print("Alcanzado el número máximo de objetivos.")

    def calculate_detailed_plan(self) -> dict[str, list[str]]:
        """Calculates the purpose plan"""
        detailed_plan_list: dict[str, list[str]] = {"Enero": [], "Febrero": [], "Marzo": [], "Abril": [], "Mayo": [
        ], "Junio": [], "Julio": [], "Agosto": [], "Septiembre": [], "Octubre": [], "Noviembre": [], "Diciembre": []}

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for i, purpose in enumerate(self.purposes_list):
            for j in range(purpose.term):
                detailed_plan_list[months[j]].append(
                    f"[ ] {i+1}. {purpose.target} ({purpose.amount // purpose.term} {purpose.units}/mes). Total: {purpose.amount}")

        return detailed_plan_list

    def show_plan(self, plan_list: dict[str, list[str]]) -> None:
        """Shows the plan to the screen"""
        for plan, purposes in plan_list.items():
            if purposes:
                print(f"\n{plan}:")
                for purpose in purposes:
                    print(purpose)

    def export_plan(self, plan_list: dict[str, list[str]]) -> None:
        """Exports the plan to a file"""
        with open("detailed_plan.txt", "w", encoding="utf-8") as f:
            for plan, purposes in plan_list.items():
                if purposes:
                    f.write(f"{plan}:\n")
                    for purpose in purposes:
                        f.write(f"{purpose}\n")


def user_iput() -> tuple[str, int, str, int]:
    """Gets the user plan"""

    objetivo: str = input("Introduce tu objetivo: ")

    while True:
        try:
            cantidad: int = int(input("Introduce la cantidad del objetivo: "))
            break
        except ValueError:
            print()

    unidad: str = input("Introduce la unidad del objetivo: ")

    while True:
        try:
            plazo: int = int(input(
                "Introduce el plazo en meses a cumplir el objetivo (máximo 12): "))
            if 0 < plazo < 13:
                break
        except ValueError:
            print("Por favor introduce un entero entre 1 y 12")

    return (objetivo, cantidad, unidad, plazo)


def menu(objetivos: PurposesManagement) -> None:
    """Shows the menu and calls the methods"""
    while True:

        print("\nOpciones:")
        print("1 - Añadir objetivo")
        print("2 - Mostrar plan")
        print("3 - Exportar plan")
        print("0 - Salir")

        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "1":
                objetivo, cantidad, unidad, plazo = user_iput()
                objetivos.add_purpose(objetivo, cantidad, unidad, plazo)
            case "2":
                plan_list = objetivos.calculate_detailed_plan()
                objetivos.show_plan(plan_list)
            case "3":
                plan_list = objetivos.calculate_detailed_plan()
                objetivos.export_plan(plan_list)
            case "0":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")


def main():
    """Main function"""
    objetivos = PurposesManagement()

    menu(objetivos)


if __name__ == "__main__":
    main()
