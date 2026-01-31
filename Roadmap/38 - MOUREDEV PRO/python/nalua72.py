
import csv
import random
from pathlib import Path

"""
/*
 * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */
"""

CSV_FILE = "usuarios.csv"


def generate_csv_file() -> None:
    """Genera un CSV con usuarios ficticios."""
    header = ["id", "email", "status"]

    rows = []
    for i in range(1, 101):
        rows.append({
            "id": str(i),
            "email": f"test{i}@test.com",
            "status": random.choice(["active", "inactive"])
        })

    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def read_csv_candidates() -> list[dict]:
    """Lee el CSV y devuelve los usuarios como diccionarios."""
    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def select_winners(users: list[dict], num_winners: int = 3) -> list[dict]:
    """Selecciona ganadores activos y no repetidos."""
    active_users = [u for u in users if u["status"] == "active"]

    if len(active_users) < num_winners:
        raise ValueError("No hay suficientes usuarios activos para el sorteo")

    return random.sample(active_users, num_winners)


def main() -> None:
    if not Path(CSV_FILE).exists():
        generate_csv_file()

    users = read_csv_candidates()
    ganador_suscripcion, ganador_descuento, ganador_libro = select_winners(
        users)

    print(
        f"🎉 Suscripción → id: {ganador_suscripcion['id']} | email: {ganador_suscripcion['email']}"
    )
    print(
        f"🏷️ Descuento → id: {ganador_descuento['id']} | email: {ganador_descuento['email']}"
    )
    print(
        f"📘 Libro → id: {ganador_libro['id']} | email: {ganador_libro['email']}"
    )


if __name__ == "__main__":
    main()
