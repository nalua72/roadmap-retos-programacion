import calendar
from dataclasses import dataclass

"""
/*
 * EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre...
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
 * su 100 aniversario.
 *
 * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva.
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas.
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada (x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones:
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad.
 */
"""


def third_saturday(year, month=9):
    # Obtenemos todos los días de la semana del mes
    month_calendar = calendar.monthcalendar(year, month)

    saturdays = []
    for week in month_calendar:
        if week[calendar.SATURDAY] != 0:  # si hay sábado en la semana
            saturdays.append(week[calendar.SATURDAY])

    # El tercer sábado
    return saturdays[2]


def batman_day():
    for year in range(2026, 2040):
        batmanday = third_saturday(year)
        print(
            f"En el año {year} el Batman Day se celebra el {batmanday} de septiembre")


@dataclass
class CaveSensors():
    """Contiene los sensores de amenaza de Gotham"""
    sensors: list[tuple[int, int, int]]


class BatmanCave():
    SECURITY_THRESHOLD = 20

    def __init__(self) -> None:
        """Inicializa la matriz de la cueva"""
        self.cave = [[0 for _ in range(20)] for _ in range(20)]

    def put_sensors(self, sensors: CaveSensors) -> None:
        """Coloca los sensores en la matriz"""
        for x, y, threat in sensors.sensors:
            self.cave[x][y] += threat

    def calculate_threat(self, coordinate: tuple[int, int]) -> int:
        """Calcula la amenaza de una cuadricula de 3x3"""
        threat: int = 0

        x = coordinate[0]
        y = coordinate[1]

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                threat += self.cave[x + dx][y + dy]

        return threat

    def most_dangerous_area(self) -> tuple[tuple[int, int], int]:
        """Calcula el area 3x3 mas peligrosa. Devuelve la coordenada centgral de ese area y el grado de amenaza"""
        max_threat: int = 0
        coordinate: tuple[int, int] = (1, 1)

        for x in range(1, 19):
            for y in range(1, 19):
                threat = self.calculate_threat((x, y))
                if threat > max_threat:
                    max_threat = threat
                    coordinate = (x, y)

        return coordinate, max_threat

    def security_report(self) -> None:
        """Calcula e informa d elas areas de peligro"""

        area_coordinates, threat = self.most_dangerous_area()

        distance = self.calculate_distance(area_coordinates)

        if threat < self.SECURITY_THRESHOLD:
            print(
                f"No se detectan amenazas serias. Hay una amenaza máxima de grado {threat} a la distancia {distance} en el área {area_coordinates}.")

            print(f"")
            return

        print(
            f"Todas los recursos al área {area_coordinates} a la distancia {distance}. Hay una amenaza de grado {threat}")

    def calculate_distance(self, coordinate: tuple[int, int]) -> int:
        """Calcula la distancia Manhattan de una celda a la celda (0,0)"""
        return abs(coordinate[0]) + abs(coordinate[1])


def main():
    """ Reto 1"""
    batman_day()

    """ Reto 2"""
    sensores = CaveSensors(
        sensors=[
            (2, 3, 5),
            (4, 3, 6),
            (2, 2, 7),
            (10, 12, 8),
            (15, 18, 4)
        ]
    )
    batman_cave = BatmanCave()

    batman_cave.put_sensors(sensores)
    batman_cave.security_report()


if __name__ == "__main__":
    main()
