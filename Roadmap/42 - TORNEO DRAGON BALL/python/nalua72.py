import random
from dataclasses import dataclass, field

"""
/*
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
 */
"""


@dataclass
class Fighter:
    """Class to define a fighter"""
    name: str
    velocity: int
    attack: int
    defense: int
    health: int = 100


class Round:
    """Class to store the status of each round"""

    def __init__(self, number: int, fighters: list[Fighter]) -> None:
        self.number = number
        self.fighters = fighters.copy()
        self.combats: list[tuple[Fighter, Fighter]] = []
        self.winners: list[Fighter] = []

    def run(self) -> None:
        """Method to run a round"""
        message = TournamentPrint()
        self.combats = self._generate_draft(self.fighters)
        message.round_pairs(self.number, self.combats)

        for combat_pairs in self.combats:
            battle = Battle(combat_pairs)
            winner = battle.fight()
            winner.health = 100
            self.winners.append(winner)

    def _generate_draft(self, fighters: list[Fighter]) -> list[tuple[Fighter, Fighter]]:
        """Creates a list of tuples of fighters"""
        fighters = fighters.copy()
        random.shuffle(fighters)

        return [
            (fighters[i], fighters[i + 1])
            for i in range(0, len(fighters), 2)
        ]


class Battle:
    """Class to manage a battle"""

    def __init__(self, fighters: tuple[Fighter, Fighter]) -> None:
        self.attacker, self.defensor = fighters

    def fight(self) -> Fighter:
        """Method to calculate the winner of a fight"""
        message = TournamentPrint()
        self._initial_attacker()

        while self.attacker.health > 0 and self.defensor.health > 0:
            if random.random() < 0.2:
                message.avoids_attack(self.attacker, self.defensor)
                self.attacker, self.defensor = self.defensor, self.attacker
                continue

            damage = self.attacker.attack - self.defensor.defense

            if damage <= 0:
                damage = self.attacker.attack * 0.1

            self.defensor.health = max(0, self.defensor.health - damage)

            message.battle_state(self.attacker, self.defensor, damage)

            self.attacker, self.defensor = self.defensor, self.attacker

        return self.attacker if self.attacker.health > 0 else self.defensor

    def _initial_attacker(self):
        """Method to decide who attacks first"""
        if self.defensor.velocity > self.attacker.velocity:
            self.attacker, self.defensor = self.defensor, self.attacker


class Tournament:
    """Class to manage the tournament"""

    def __init__(self):
        self.initial_fighters: list[Fighter] = []
        self.current_fighters: list[Fighter] = []
        self.rounds: list[Round] = []
        self.round_number = 1

    def register_participant(self, name: str):
        """Method to register fighters"""
        velocity = random.randint(1, 100)
        attack = random.randint(1, 100)
        defense = random.randint(1, 100)

        fighter = Fighter(name=name, velocity=velocity,
                          attack=attack, defense=defense)

        # Avoids to have duplicated fighters
        if any(fighter.name == f.name for f in self.initial_fighters):
            raise ValueError("Ya existe ese luchador")
        else:
            self.initial_fighters.append(fighter)

        return self.initial_fighters

    def start(self):
        """Method to run a tournament"""
        messages = TournamentPrint()

        if not self._is_power_of_two(len(self.initial_fighters)):
            raise ValueError("No hay luchadores suficientes")

        messages.initial_message(self.initial_fighters)

        self.current_fighters = self.initial_fighters

        while len(self.current_fighters) > 1:

            round = Round(number=self.round_number,
                          fighters=self.current_fighters)

            round.run()
            messages.round_winners(round)

            self.rounds.append(round)
            self.current_fighters = round.winners
            self.round_number += 1

        messages.winner_message(round.winners[0])

    def _is_power_of_two(self, n: int) -> bool:
        """returns True if number is power of 2"""
        return n > 0 and (n & (n - 1)) == 0


class TournamentPrint:
    """Class to manage user prints"""

    def initial_message(self, fighters: list[Fighter]) -> None:
        print("*************EMPIEZA EL TORNEO***********")
        print()
        print("La lista de luchadores que se presentan al torneo son:\n")

        for fighter in fighters:
            print(fighter.name)

    def avoids_attack(self, attacker: Fighter, defensor: Fighter) -> None:
        print(f"{defensor.name} esquivó el ataque de {attacker.name}")

    def battle_state(self, attacker: Fighter, defensor: Fighter, damage: float) -> None:
        print(
            f"{attacker.name} golpea a {defensor.name} "
            f"y le hace {damage:.1f} de daño "
            f"(vida restante ({defensor.name}): {defensor.health:.1f})"
        )

    def round_pairs(self, number: int, combats: list[tuple[Fighter, Fighter]]) -> None:
        print(f"Los emparejaminetos de la ronda {number} son:")
        for combat in combats:
            print(f"{combat[0].name} vs {combat[1].name}")

    def round_winners(self, round: Round) -> None:
        print(f"Los ganadores de la ronda {round.number} son:")
        for winners in round.winners:
            print(winners.name)

    def winner_message(self, fighter: Fighter) -> None:
        print(f"El ganador del torneo es: {fighter.name}")


def main():
    torneo = Tournament()

    luchadores = ["Son Goku", "Krilin", "Piccolo",
                  "Tortuga", "Chaoz", "Cell", "Raditz", "Butta"]

    for luchador in luchadores:
        torneo.register_participant(luchador)

    torneo.start()


if __name__ == "__main__":
    main()
