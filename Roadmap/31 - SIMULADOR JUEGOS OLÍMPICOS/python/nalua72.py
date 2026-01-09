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
    """
    Entidad de dominio que representa a un participante olímpico.

    - Es INMUTABLE (frozen=True) para evitar cambios accidentales.
    - No contiene lógica de negocio: solo datos.
    - Identificado de forma única por su id.

    Principios:
    - SRP: solo representa un participante.
    - Inmutabilidad = más seguridad.
    """
    id: int
    name: str
    country: str


@dataclass
class Event:
    """
    Entidad de dominio que representa un evento deportivo.

    - Contiene solo información básica.
    - La lógica relacionada con eventos vive en los controllers.
    """
    id: int
    name: str


class Medal(Enum):
    """
    Enumeración que define los tipos de medalla posibles.

    - Evita strings mágicos.
    - Hace el código más seguro y legible.
    """
    GOLD = "Oro"
    SILVER = "Plata"
    BRONZE = "Bronce"


@dataclass
class EventResult:
    """
    Representa el resultado de un participante en un evento concreto.

    - Relaciona evento + participante + posición.
    - La medalla puede ser None si no entra en el podio.
    """
    event_id: int
    participant: Participant
    position: int
    medal: Medal | None


@dataclass
class CountryMedalCount:
    """
    DTO (Data Transfer Object) para agrupar medallas por país.

    - Se usa únicamente en la generación de informes.
    - No se persiste como entidad principal.
    """
    country: str
    gold: int = 0
    silver: int = 0
    bronze: int = 0


# Capa de repositorios


class ParticipantRepository:
    """
    Repositorio responsable de almacenar y recuperar participantes.

    - NO contiene lógica de negocio.
    - Encapsula la estructura de datos interna.

    Principios:
    - SRP: solo gestiona participantes.
    - Encapsulación: nadie accede a _participants directamente.
    """

    def __init__(self):
        self._participants: list[Participant] = []
        self._next_id = 100  # Generador de IDs únicos

    def add(self, name: str, country: str) -> Participant | None:
        """
        Crea y almacena un nuevo participante.

        - Verifica duplicados por nombre + país.
        - Devuelve None si ya existe (regla de negocio simple).
        """

        if any(p.name == name and p.country == country for p in self._participants):
            return None

        participant = Participant(self._next_id, name, country)
        self._participants.append(participant)
        self._next_id += 1
        return participant

    def get_all(self) -> list[Participant]:
        """
        Devuelve una copia de los participantes registrados.

        - Se devuelve copia para evitar modificaciones externas.
        """
        return self._participants.copy()  # Copia para proteger la lista interna

    def get_by_id(self, participant_id: int) -> Participant | None:
        """Busca un participante por ID. Devuelve None si no existe."""
        return next((p for p in self._participants if p.id == participant_id), None)


class EventRepository:
    """
    Repositorio encargado de gestionar eventos deportivos.

    - Evita duplicados por nombre (case-insensitive).
    """

    def __init__(self):
        self._events: list[Event] = []
        self._next_id = 100  # Generador de IDs únicos

    def add(self, name: str) -> Event | None:
        """Crea un Event, lo guarda y devuelve la instancia."""
        if any(e.name.lower() == name.lower() for e in self._events):
            return None

        event = Event(self._next_id, name)
        self._events.append(event)
        self._next_id += 1
        return event

    def get_all(self) -> list[Event]:
        """Devuelve todos los eventos registrados."""
        return self._events.copy()  # Copia para proteger la lista interna

    def get_by_id(self, event_id: int) -> Event | None:
        """Busca un evento por ID. Devuelve None si no existe."""
        return next((e for e in self._events if e.id == event_id), None)


class EventRegistrationRepository:
    """
    Repositorio que gestiona la inscripción de participantes en eventos.

    Estructura:
    - dict[event_id] -> list[Participant]

    Nota:
    - Un participante puede estar en varios eventos.
    - No se guarda lógica de validación aquí.
    """

    def __init__(self):
        self._registrations: dict[int, list[Participant]] = {}

    def register(self, event_id: int, participant: Participant) -> bool:
        participants = self._registrations.setdefault(event_id, [])

        if participant in participants:
            return False

        participants.append(participant)
        return True

    def get_participants(self, event_id: int) -> list[Participant]:
        return self._registrations.get(event_id, []).copy()


class EventResultRepository:
    """
    Repositorio encargado de almacenar los resultados de los eventos.

    - Permite borrar resultados de un evento para re-simular.
    - Separa claramente resultados de inscripciones.
    """

    def __init__(self):
        self._results: list[EventResult] = []

    def add(self, event_id: int, participant: Participant, position: int, medal: Medal | None):
        self._results.append(EventResult(
            event_id, participant, position, medal))

    def clear_event(self, event_id: int):
        """Borra un EventResult de la lista"""
        self._results = [r for r in self._results if r.event_id != event_id]

    def get_by_event(self, event_id: int) -> list[EventResult]:
        """Busca los resultados de un evento por el id del evento"""
        return [r for r in self._results if r.event_id == event_id]

    def get_all(self) -> list[EventResult]:
        """Devuelve todos los resultados registrados."""
        return self._results.copy()  # Copia para proteger la lista interna


# Capa de CONTROLLERS
class ParticipantController:
    """
    Controlador que orquesta la lógica relacionada con participantes.

    - Valida reglas.
    - Comunica mensajes al usuario.
    - Usa el repository como dependencia.

    Principios:
    - DIP: depende de una abstracción (repository).
    """

    def __init__(self, repository: ParticipantRepository):
        self._repository = repository

    def register(self, name: str, country: str) -> Participant | None:
        """
        Registra un nuevo participante.

        - Aplica reglas de negocio.
        - Traduce errores técnicos en mensajes entendibles.
        """

        participant = self._repository.add(name, country)

        if participant is None:
            print("❌ Ya existe un participante con ese nombre y país")
            return None

        print("✅ Participante registrado correctamente")
        return participant

    def list_participants(self) -> list[Participant]:
        """Devuelve la lista completa de participantes."""
        return self._repository.get_all()


class EventController():
    """
    Controlador para la gestión de eventos deportivos.
    """

    def __init__(self, repository: EventRepository):
        self._repository = repository

    def register(self, event: str) -> Event | None:
        """
        Registra un evento.
        - Crea el evento con ID generado por el repository.
        - Devuelve la instancia registrada.
        """
        event = self._repository.add(event)

        if event is None:
            print("❌ Ya existe un evento con ese nombre")
            return None

        print("✅ Evento registrado correctamente")
        return event

    def list_events(self) -> list[Event]:
        """Devuelve la lista completa de eventos."""
        return self._repository.get_all()


class EventRegistrationController:
    """
    Controlador encargado de inscribir participantes en eventos.

    - Valida existencia de evento y participante.
    - Garantiza coherencia del sistema.
    """

    def __init__(self, event_repo: EventRepository, participant_repo: ParticipantRepository, registration_repo: EventRegistrationRepository):
        self.event_repo = event_repo
        self.participant_repo = participant_repo
        self.registration_repo = registration_repo

    def register_participant(self, event_id: int, participant_id: int) -> bool:
        event = self.event_repo.get_by_id(event_id)
        participant = self.participant_repo.get_by_id(participant_id)

        if event is None:
            print("❌ El evento no existe")
            return False

        if participant is None:
            print("❌ El participante no existe")
            return False

        success = self.registration_repo.register(event_id, participant)

        if not success:
            print("❌ El participante ya está inscrito en este evento")
            return False

        print(f"✅ {participant.name} inscrito en {event.name}")
        return True


class SimulationController:
    """
    Controlador responsable de la simulación de los eventos.

    - Simula TODOS los eventos registrados.
    - Aplica reglas mínimas (>= 3 participantes).
    - Asigna posiciones y medallas.
    """

    def __init__(
        self,
        events: EventRepository,
        registrations: EventRegistrationRepository,
        results: EventResultRepository
    ):
        self.events = events
        self.registrations = registrations
        self.results = results

    def simulate_all_events(self):
        """
        Simula todos los eventos disponibles.

        - Ignora eventos no válidos.
        - No rompe la ejecución global.
        """
        for event in self.events.get_all():
            participants = self.registrations.get_participants(event.id).copy()

            if len(participants) < 3:
                print(
                    f"⚠️ '{event.name}' no se puede simular (menos de 3 participantes)")
                continue

            print(f"▶️ Simulando evento: {event.name}")
            self._simulate_event(event.id, participants)

    def _simulate_event(self, event_id: int, participants: list[Participant]):
        self.results.clear_event(event_id)
        random.shuffle(participants)

        for pos, participant in enumerate(participants, start=1):
            medal = self._assign_medal(pos)
            self.results.add(event_id, participant, pos, medal)

    def _assign_medal(self, pos: int) -> Medal | None:
        return {
            1: Medal.GOLD,
            2: Medal.SILVER,
            3: Medal.BRONZE
        }.get(pos)


class ReportController():
    """
    Controlador encargado de generar informes.

    - No modifica estado.
    - Solo lee datos y los presenta.

    Principio:
    - CQRS ligero (lectura separada de escritura).
    """

    def __init__(self, events: EventRepository, results: EventResultRepository):
        self.events = events
        self.results = results

    def show_event_winners(self):
        for event in self.events.get_all():
            winners = sorted(self.results.get_by_event(
                event.id), key=lambda r: r.position)[:3]

            if not winners:
                continue

            print(f"\n🏅 {event.name}")
            for r in winners:
                print(
                    f"{r.position}. {r.participant.name} ({r.participant.country})")

    def show_country_ranking(self):
        country_map: dict[str, CountryMedalCount] = {}

        for result in self.results.get_all():
            country = result.participant.country
            country_map.setdefault(country, CountryMedalCount(country))

            if result.medal == Medal.GOLD:
                country_map[country].gold += 1
            elif result.medal == Medal.SILVER:
                country_map[country].silver += 1
            elif result.medal == Medal.BRONZE:
                country_map[country].bronze += 1

        ranking = sorted(
            country_map.values(),
            key=lambda c: (c.gold, c.silver, c.bronze),
            reverse=True
        )

        print("\n🌍 Ranking por países")
        for c in ranking:
            print(f"{c.country}: 🥇{c.gold} 🥈{c.silver} 🥉{c.bronze}")


class MainMenuController():
    """
    Composition Root de la aplicación.

    - Crea repositorios.
    - Inyecta dependencias.
    - Coordina el flujo general.

    IMPORTANTE:
    👉 Es el ÚNICO lugar donde se instancia todo.
    """

    def __init__(self):
        self.participants = ParticipantRepository()
        self.events = EventRepository()
        self.registrations = EventRegistrationRepository()
        self.results = EventResultRepository()

        self.participant_ctrl = ParticipantController(self.participants)
        self.event_ctrl = EventController(self.events)
        self.registration_ctrl = EventRegistrationController(
            self.events, self.participants, self.registrations)
        self.simulation_ctrl = SimulationController(
            self.events, self.registrations, self.results)
        self.report_ctrl = ReportController(self.events, self.results)

        self.run()

    def run(self):
        while True:
            self._show_menu()

            opcion = MenuInputHandler().get_option()
            self.handle_option(opcion)

    def _show_menu(self):
        MenuRenderer().render_menu()

    def handle_option(self, option):
        """
        Orquesta las acciones según la opción del menú.

        - No contiene lógica compleja.
        - Delegación total a controllers especializados.
        """
        match option:
            case 1:
                evento = EventInputHandler().get_event()
                self.event_ctrl.register(evento)
            case 2:
                participante = ParticipantInputHandler()
                name = participante.get_participant_name()
                country = participante.get_participant_country()

                event_id = participante.get_event_id(self.events)
                if event_id is None or self.events.get_by_id(event_id) is None:
                    print("❌ El evento seleccionado no existe")
                    return

                participant = self.participant_ctrl.register(name, country)
                if participant is None:
                    return

                self.registration_ctrl.register_participant(
                    event_id, participant.id)
            case 3:
                self.simulation_ctrl.simulate_all_events()

            case 4:
                self.report_ctrl.show_event_winners()
                self.report_ctrl.show_country_ranking()
            case 5:
                print("Saliendo....")
                exit(0)
            case _:
                print("Escoge una opcion del 1 al 5")

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
    """
    Responsable EXCLUSIVO de pedir datos al usuario.

    - No valida negocio.
    - No accede a repositorios.

    SRP en estado puro.
    """

    def get_participant_name(self) -> str:
        return input("Nombre del participante: ")

    def get_participant_country(self) -> str:
        return input("País del participante: ")

    def get_event_id(self, events: EventRepository) -> int | None:
        event_list = events.get_all()

        if not event_list:
            print("❌ No hay eventos disponibles")
            return None

        print("Eventos disponibles:")
        for e in event_list:
            print(f"{e.id} - {e.name}")

        try:
            return int(input("Evento id por favor: "))
        except ValueError:
            print("Por favor, escoge un número.")
            return None

# Capa de renderizacion


class MenuRenderer():
    """
    Se encarga únicamente de mostrar el menú.

    Ventaja:
    - Fácil de cambiar UI sin tocar lógica.
    """

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
