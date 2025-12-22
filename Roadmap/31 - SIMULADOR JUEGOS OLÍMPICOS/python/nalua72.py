import random
from dataclasses import dataclass
from enum import Enum

"""
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
"""


# Entidades del dominio


@dataclass(frozen=True)
class Participant():
    id: int
    name: str
    country: str


@dataclass
class Event:
    id: int
    name: str


class Medal(Enum):
    GOLD = "Oro"
    SILVER = "Plata"
    BRONZE = "Bronce"


@dataclass
class EventResult:
    event_id: int
    participant: Participant
    position: int
    medal: Medal | None


@dataclass
class CountryMedalCount:
    country: str
    gold: int = 0
    silver: int = 0
    bronze: int = 0


# Capa de repositorios

# Gestión de participantes
class ParticipantRepository:
    def __init__(self):
        self._participants: list[Participant] = []
        self._next_id = 100  # Generador de IDs únicos

    def add(self, name: str, country: str) -> Participant:
        """Crea un Participant, lo guarda y devuelve la instancia."""
        participant = Participant(id=self._next_id, name=name, country=country)
        self._participants.append(participant)
        self._next_id += 1
        return participant

    def get_all(self) -> list[Participant]:
        """Devuelve todos los participantes registrados."""
        return self._participants.copy()  # Copia para proteger la lista interna

    def get_by_id(self, participant_id: int) -> Participant | None:
        """Busca un participante por ID. Devuelve None si no existe."""
        for p in self._participants:
            if p.id == participant_id:
                return p
        return None

    def exists(self, participant_id: int) -> bool:
        """Comprueba si existe un participante con un ID dado."""
        return any(p.id == participant_id for p in self._participants)


# Gestión de eventos
class EventRepository:
    def __init__(self):
        self._events: list[Event] = []
        self._next_id = 100  # Generador de IDs únicos

    def add(self, name: str) -> Event:
        """Crea un Event, lo guarda y devuelve la instancia."""
        event = Event(id=self._next_id, name=name)
        self._events.append(event)
        self._next_id += 1
        return event

    def get_all(self) -> list[Event]:
        """Devuelve todos los eventos registrados."""
        return self._events.copy()  # Copia para proteger la lista interna

    def get_by_id(self, event_id: int) -> Event | None:
        """Busca un evento por ID. Devuelve None si no existe."""
        for p in self._events:
            if p.id == event_id:
                return p
        return None

    def exists(self, event_id: int) -> bool:
        """Comprueba si existe un evento con un ID dado."""
        return any(p.id == event_id for p in self._events)

# Gestion de resultados


class EventResultRepository:
    def __init__(self):
        self._event_results: list[EventResult] = []

    def add(self, event_id: int, participant: Participant, position: int, medal: Medal) -> EventResult:
        """Crea un EventResult, lo guarda y devuelve la instancia."""
        result = EventResult(
            event_id=event_id, participant=participant, position=position, medal=medal)
        self._event_results.append(result)
        return result

    def get_by_event(self, event_id: int) -> list[EventResult]:
        """Busca los resultados de un evento. Devuelve lista vacia si no existe."""
        results_list = []
        for e in self._event_results:
            if e.event_id == event_id:
                results_list.append(e)
        return results_list

    def get_all(self) -> list[EventResult]:
        """Devuelve todos los resultados registrados."""
        return self._event_results.copy()  # Copia para proteger la lista interna

    def clear_event(self, event_id: int) -> None:
        """Borra un EventResult de la lista"""
        self._event_results = list(
            filter(lambda x: x.event_id != event_id, self._event_results))


# Capa de Presentacion: (Controllers + InputHandlers + Renderers)


class MainMenuController():
    def __init__(self):
        self.participant_repository = ParticipantRepository()
        self.event_repository = EventRepository()
        self.event_result_repository = EventResultRepository()

        self.participant_controller = ParticipantController(
            self.participant_repository)
        self.event_controller = EventController(self.event_repository)
        self.simulation_controller = SimulationController(
            results=self.event_result_repository,
            events=self.event_repository,
            participants=self.participant_repository
        )
        self.report_controller = ReportController(
            events=self.event_repository, events_result=self.event_result_repository)

        self.run()

    def run(self):
        while True:
            self._show_menu()

            opcion = MenuInputHandler().get_option()
            self.handle_option(opcion)

    def _show_menu(self):
        MenuRenderer().render_menu()

    def handle_option(self, option):
        match option:
            case 1:
                evento = EventInputHandler().get_event()
                event = self.event_controller.register_event(evento)
                print(f"Evento registrado: {event}")
            case 2:
                participante = ParticipantInputHandler()
                name = participante.get_participant_name()
                country = participante.get_participant_country()

                participant = self.participant_controller.register_participant(
                    name, country)
                print(f"Participante registrado: {participant}")
            case 3:
                handler = SimulationInputHandler()
                event_id = handler.get_event_id()
                if event_id is None:
                    return

                success = self.simulation_controller.simulate_event(event_id)

                if not success:
                    print(
                        "No se pudo simular el evento (evento inexistente o pocos participantes)")
                else:
                    print("Evento simulado correctamente")

            case 4:
                print("Creación de informes")
                event_list = self.event_controller.list_events()

                for event in self.event_controller.list_events():
                    winners = self.report_controller.show_event_winners(
                        event.id)
                    WinnersByEventRenderer().render_winners_by_event(winners)
                country_ranking = self.report_controller.show_country_ranking()
                RankingByCountryRenderer().render_ranking_by_country(country_ranking)
            case 5:
                print("Saliendo....")
                exit(0)
            case _:
                print("Escoge una opcion del 1 al 5")


class EventController():
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def register_event(self, event: str) -> Event:
        """
        Registra un evento.
        - Crea el evento con ID generado por el repository.
        - Devuelve la instancia registrada.
        """
        return self._repository.add(event)

    def list_events(self) -> list[Event]:
        """Devuelve la lista completa de eventos."""
        return self._repository.get_all()

# Capa de lógica de negocio: orquesta los casos de uso de participantes


class ParticipantController:
    def __init__(self, repository: ParticipantRepository):
        self._repository = repository

    def register_participant(self, name: str, country: str) -> Participant:
        """
        Registra un participante.
        - Crea el participante con ID generado por el repository.
        - Devuelve la instancia registrada.
        """
        return self._repository.add(name, country)

    def list_participants(self) -> list[Participant]:
        """Devuelve la lista completa de participantes."""
        return self._repository.get_all()


class SimulationController():
    def __init__(self, results: EventResultRepository, events: EventRepository, participants: ParticipantRepository):
        self.results = results
        self.events = events
        self.participants = participants

    def simulate_event(self, event_id: int) -> bool:
        event = self._event_exists(event_id)
        participants = self._get_participants()

        if event is None or not participants:
            return False

        self.results.clear_event(event_id)

        participants_random = self._random_simulate(participants)

        for pos, participant in enumerate(participants_random, start=1):
            participant_position = pos
            participant_medal = self._assign_medal(participant_position)
            self._add_event_result(event_id, participant,
                                   participant_position, participant_medal)
        return True

    def _event_exists(self, event_id: int) -> Event | None:
        """Devuelve un Event si existe, None si no existe"""
        event = self.events.get_by_id(event_id)
        return event

    def _get_participants(self) -> list[Participant]:
        """Devuelve una lista de participantes si es mayor que 2"""
        participants = self.participants.get_all()
        if len(participants) < 3:
            return []
        return participants

    def _random_simulate(self, participants: list[Participant]) -> list[Participant]:
        shuffled = participants.copy()
        random.shuffle(shuffled)
        return shuffled

    def _assign_medal(self, position: int) -> Medal | None:
        if position == 1:
            return Medal.GOLD
        if position == 2:
            return Medal.SILVER
        if position == 3:
            return Medal.BRONZE
        return None

    def _add_event_result(self,
                          event_id: int,
                          participant: Participant,
                          position: int,
                          medal: Medal) -> None:
        self.results.add(
            event_id, participant, position, medal)


class ReportController():
    def __init__(self, events: EventRepository, events_result: EventResultRepository):
        self.events = events
        self.events_result = events_result

    def show_event_winners(self, event_id) -> list[EventResult]:
        results_list = self._get_results_by_event(event_id)
        results_list.sort(key=lambda r: r.position)
        return results_list[:3]

    def show_country_ranking(self) -> list[CountryMedalCount]:
        countries_map = self._group_results_by_country()
        medal_table = self._build_country_medal_table(countries_map)
        return self._sort_countries_by_medal(medal_table)

    def _get_results_by_event(self, event_id: int) -> list[EventResult]:
        return self.events_result.get_by_event(event_id)

    def _group_results_by_country(self) -> dict[str, list[EventResult]]:
        country_map: dict[str, list[EventResult]] = {}

        for result in self.events_result.get_all():
            country = result.participant.country

            if country not in country_map:
                country_map[country] = []

            country_map[country].append(result)

        return country_map

    def _build_country_medal_table(
        self, countries: dict[str, list[EventResult]]
    ) -> list[CountryMedalCount]:

        country_medal_table: list[CountryMedalCount] = []

        for country, event_results in countries.items():
            country_medal = CountryMedalCount(country)

            for result in event_results:
                if result.medal == Medal.GOLD:
                    country_medal.gold += 1
                elif result.medal == Medal.SILVER:
                    country_medal.silver += 1
                elif result.medal == Medal.BRONZE:
                    country_medal.bronze += 1

            country_medal_table.append(country_medal)

        return country_medal_table

    def _sort_countries_by_medal(self, countries: list[CountryMedalCount]
                                 ) -> list[CountryMedalCount]:
        return sorted(
            countries,
            key=lambda c: (c.gold, c.silver, c.bronze),
            reverse=True
        )
# Capa de Input handlers


class MenuInputHandler():
    def get_option(self) -> int | None:
        try:
            return int(input("Escoge una opción: "))
        except ValueError:
            print("Por favor, escoge un número.")
            return None


class EventInputHandler():
    def get_event(self) -> str:
        return input("Nombre del evento: ")


class ParticipantInputHandler():
    def get_participant_name(self) -> str:
        return input("Nombre del participante: ")

    def get_participant_country(self) -> str:
        return input("País del participante: ")


class SimulationInputHandler():
    def get_event_id(self) -> int | None:
        try:
            return int(input("Evento id por favor: "))
        except ValueError:
            print("Por favor, escoge un número.")
            return None

# Capa de renderizacion


class MenuRenderer():
    def render_menu(self):
        print("Acciones:\n"
              "1. Registro de eventos.\n"
              "2. Registro de participantes.\n"
              "3. Simulación de eventos.\n"
              "4. Creación de informes.\n"
              "5. Salir del programa.\n"
              )


class RankingByCountryRenderer():
    def render_ranking_by_country(self, country_map: list[CountryMedalCount]) -> None:
        print("Informe de medallas por pais")
        for country in country_map:
            print(f"Pais: {country.country}")
            print(f"\tMedallas de oro: {country.gold}")
            print(f"\tMedallas de plata: {country.silver}")
            print(f"\tMedallas de bronce: {country.bronze}")


class WinnersByEventRenderer():
    def render_winners_by_event(self, result_list: list[EventResult]) -> None:
        print("Informe de ganadores por eventos")
        if not result_list:
            return

        print(f"Ranking del evento {result_list[0].event_id}")

        for result in result_list:
            print(
                f"\t{result.position}. {result.participant.name} "
                f"({result.participant.country})"
            )


def main():
    MainMenuController()


if __name__ == "__main__":
    main()
