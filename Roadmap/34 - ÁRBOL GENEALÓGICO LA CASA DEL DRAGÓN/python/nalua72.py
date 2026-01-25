from dataclasses import dataclass, field
"""
 * EJERCICIO:
 * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
 * ¿Alguien se entera de todas las relaciones de parentesco
 * entre personajes que aparecen en la saga?
 * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
 * Requisitos:
 * 1. Estará formado por personas con las siguientes propiedades:
 *    - Identificador único (obligatorio)
 *    - Nombre (obligatorio)
 *    - Pareja (opcional)
 *    - Hijos (opcional)
 * 2. Una persona sólo puede tener una pareja (para simplificarlo).
 * 3. Las relaciones deben validarse dentro de lo posible.
 *    Ejemplo: Un hijo no puede tener tres padres.
 * Acciones:
 * 1. Crea un programa que permita crear y modificar el árbol.
 *    - Añadir y eliminar personas
 *    - Modificar pareja e hijo
 * 2. Podrás imprimir el árbol (de la manera que consideres).
 *
 * NOTA: Ten en cuenta que la complejidad puede ser alta si
 * se implementan todas las posibles relaciones. Intenta marcar
 * tus propias reglas y límites para que te resulte asumible.
"""


@dataclass
class FamilyMember:
    id: int
    name: str
    couple: int = None
    children: list[int] = field(default_factory=list)
    parents: list[int] = field(default_factory=list)

    def add_child(self, child_id: int):
        """Method to add a child to a member of the family"""
        if child_id not in self.children:
            self.children.append(child_id)

    def add_parent(self, parent_id: int):
        """Method to add a parent to a member of the family"""
        if parent_id not in self.parents:
            self.parents.append(parent_id)

    def set_couple(self, couple_id: int):
        """Method to assign a couple to a member of the family"""
        self.couple = couple_id


class FamilyTree:

    def __init__(self):
        self.family_tree: list[FamilyMember] = []
        self.next_id = 0

    def add_member(self, name):
        """Method to add a member to the family tree"""
        member = FamilyMember(id=self.next_id, name=name)

        self.family_tree.append(member)
        self.next_id += 1

    def remove_member(self, member_id):
        """Method to delete a member of the family tree"""
        member = self.get_member_by_id(member_id)

        if member is None:
            raise ValueError("El personaje no existe")

        # Deletes couple from the couple if exists
        if member.couple is not None:
            couple = self.get_member_by_id(member.couple)
            if couple:
                couple.couple = None

        # Deletes member from child parent list if exits
        if len(member.children) > 0:
            for child_id in member.children:
                child = self.get_member_by_id(child_id)
                if len(child.parents) > 0:
                    for parent in child.parents.copy():
                        if parent == member.id:
                            child.parents.remove(parent)

        # Deletes member from child list of parents child list if exits
        if len(member.parents) > 0:
            for parent_id in member.parents:
                parent = self.get_member_by_id(parent_id)
                if len(parent.children) > 0:
                    for child in parent.children.copy():
                        if child == member_id:
                            parent.children.remove(child)

        # Deletes member from family tree
        self.family_tree.remove(member)

    def get_member_by_id(self, member_id) -> FamilyMember:
        return next((member for member in self.family_tree if member.id == member_id), None)

    def show_family_tree(self, member_id: int, prefix="", is_last=True, visited=None):
        """Method to display family tree"""
        member: FamilyMember = self.get_member_by_id(member_id)

        if member is None:
            return

        # Avoids repeat cicles
        if visited is None:
            visited = set()

        if member_id in visited:
            print(prefix + "└── (ciclo detectado)")
            return

        visited.add(member_id)

        # Gets the couple name if exits
        if member.couple is not None:
            couple = self.get_member_by_id(member.couple)
            couple_name = couple.name if couple else "?"
            label = f"{member.name} ❤️ {couple_name}"
        else:
            label = member.name

        connector = "└── " if prefix else ""
        print(prefix + connector + label)

        new_prefix = prefix + ("    " if is_last else "│   ")

        for index, child_id in enumerate(member.children):
            last = index == len(member.children) - 1
            self.show_family_tree(child_id, new_prefix, last)

    def show_from_root(self, member_id: int):
        self.show_family_tree(member_id, prefix="",
                              is_last=True, visited=set())

    def set_couple(self, member_id: int, couple_id: int):
        """Method to assign a couple to a member of the family"""
        member: FamilyMember = self.get_member_by_id(member_id)
        couple: FamilyMember = self.get_member_by_id(couple_id)

        if couple is None or member is None:
            raise ValueError("El personaje no existe")

        member.set_couple(couple_id)
        couple.set_couple(member_id)

    def add_child(self, parent_id, child_id):
        """Method to assign a child to a member of the family"""
        parent: FamilyMember = self.get_member_by_id(parent_id)
        child: FamilyMember = self.get_member_by_id(child_id)

        if parent is None or child is None:
            raise ValueError("El personaje no existe")

        if parent == child:
            raise ValueError("El padre y el hijo no pueden ser el mismo")

        if len(child.parents) == 2:
            raise ValueError("Un personaje no puede tener más de dos padres")

        parent.add_child(child_id)
        child.add_parent(parent_id)


class InputHandler:

    def menu(self, familytre: FamilyTree):

        print("1.- Añadir un miembro de la familia")
        print("2.- Borrar un miembro de la familia")
        print("3.- Asignar una pareja a un miembro de la familia")
        print("4.- Asignar un hijo a un miembro de la familia")
        print("5.- Mostrar el árbol familiar")
        print("6.- Salir")
        print("\n")

        option = int(input("Por favor, escoge una opción (1-6): "))
        print("\n")

        match option:
            case 1:
                member_name = input("Añadir personaje: ")
                familytre.add_member(member_name)
            case 2:
                delete_member = int(input("Eliminar personaje: "))
                familytre.remove_member(delete_member)
            case 3:
                member = int(input("Asignar pareja a: "))
                pareja = int(input("ID de la pareja: "))
                try:
                    familytre.set_couple(member, pareja)
                except ValueError as e:
                    print(e)
            case 4:
                padre = int(input("Asignar hijo a: "))
                hijo = int(input("ID del hijo: "))
                try:
                    familytre.add_child(padre, hijo)
                except ValueError as e:
                    print(e)
            case 5:
                try:
                    miembro = int(input("Mostrar la familia de: "))
                    print("\n")
                    familytre.show_from_root(miembro)
                except ValueError:
                    print("Por favor escoge un número de ID")
            case 6:
                print("Salir")
                exit(0)
            case _:
                print("Opción invalida")


def main():
    familytree = FamilyTree()
    handler = InputHandler()

    print("\t\tBienvenidos al árbol genéalogico de La Casa del Dragón\n\n")

    while True:
        handler.menu(familytree)


if __name__ == "__main__":
    main()
