"""
* EJERCICIO:
* ¡Deadpool y Wolverine se enfrentan en una batalla épica!
* Crea un programa que simule la pelea y determine un ganador.
* El programa simula un combate por turnos, donde cada protagonista posee unos
* puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
* de regeneración y evasión de ataques.
* Requisitos:
* 1. El usuario debe determinar la vida inicial de cada protagonista.
* 2. Cada personaje puede impartir un daño aleatorio:
* - Deadpool: Entre 10 y 100.
* - Wolverine: Entre 10 y 120.
* 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
* siguiente turno, ya que tiene que regenerarse(pero no aumenta vida).
* 4. Cada personaje puede evitar el ataque contrario:
* - Deadpool: 25 % de posibilidades.
* - Wolverine: 20 % de posibilidades.
* 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
* Acciones:
* 1. Simula una batalla.
* 2. Muestra el número del turno(pausa de 1 segundo entre turnos).
* 3. Muestra qué pasa en cada turno.
* 4. Muestra la vida en cada turno.
* 5. Muestra el resultado final.
"""
from __future__ import annotations
from time import sleep
import random


class Character:
    """Clase para representar un personaje y sus acciones"""

    def __init__(self, name: str, life: int, harm_range: tuple[int, int], evasion: int) -> None:
        self.name = name
        self.life = life
        self.harm_range = harm_range
        self.evasion = evasion

    def attack(self) -> int:
        """Devuelve el valor del ataque"""
        return random.randint(self.harm_range[0], self.harm_range[1])

    def receive_attack(self, harm: int) -> bool:
        """Decide si un personaje recibe el ataque o lo evita"""
        evasion = self._calculate_evasion()
        if evasion:
            print(f"{self.name} evita el ataque")
            return False
        self.life = max(0, self.life - harm)
        return True

    def _calculate_evasion(self) -> bool:
        """Calculates if the character can evade the attack"""
        return random.random() < self.evasion/100


class Battle:
    """Clase que se encarga de orquestar la batalla"""

    def __init__(self, character1: Character, character2: Character) -> None:
        self.character1 = character1
        self.character2 = character2
        self.turn: int = 0
        self.locked_character: Character | None = None

    def start(self) -> None:
        """Metodo para gestionar la batalla"""
        current_attacker = random.choice([self.character1, self.character2])
        current_defender = self.character2 if current_attacker == self.character1 else self.character1

        while self._is_ongoing():
            self.turn += 1
            print(f"Turno: {self.turn}")

            # ¿Está bloqueado?
            if self.locked_character == current_attacker:
                print(f"{current_attacker.name} está bloqueado y pierde el turno")
                self.locked_character = None
            else:
                damage = current_attacker.attack()
                print(f"{current_attacker.name} ataca con fuerza {damage}")

                hit = current_defender.receive_attack(damage)

                # Regla del combate (no del personaje)
                if hit and damage == current_attacker.harm_range[1]:
                    print(f"{current_defender.name} queda bloqueado")
                    self.locked_character = current_defender

            self._print_status()

            current_attacker, current_defender = current_defender, current_attacker

            sleep(1)

    def show_final_result(self):
        """Muestra los resultados finales al acabar la batalla"""
        if self.character1.life > 0:
            ganador = self.character1.name
        else:
            ganador = self.character2.name

        print("\n\n")
        print("\t*************************************************")
        print(
            f"\t******* Ganador: {ganador.upper()} ***********************")
        print("\t*************************************************")

    def _is_ongoing(self) -> bool:
        """La batalla continua hasta que la vida de uno de los dos personajes sea 0 o menor que cero"""
        return self.character1.life > 0 and self.character2.life > 0

    def _print_status(self):
        for c in (self.character1, self.character2):
            print(f"La vida de {c.name} es {c.life}")


class InputHandler:
    """ Maneja la entrada del usuario"""

    def get_life(self, superhero: str) -> int:
        while True:
            try:
                life_input = int(input(f"Vida inicial de {superhero}: "))
                if life_input > 0:
                    return life_input
                print("Por favor, introduce un número mayor que 0")
            except ValueError:
                print("Por favor, escoge un número.")


def main():
    handler = InputHandler()

    deadpool_life = handler.get_life("Deadpool")
    wolverine_life = handler.get_life("Wolverine")

    deadpool = Character("Deadpool", deadpool_life, (10, 100), 25)
    wolverine = Character("Wolverine", wolverine_life, (10, 120), 20)

    battle = Battle(deadpool, wolverine)
    battle.start()
    battle.show_final_result()


if __name__ == "__main__":
    main()
