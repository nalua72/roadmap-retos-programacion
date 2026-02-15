import os
from datetime import datetime, timezone
from threading import Thread
from time import sleep
from zoneinfo import ZoneInfo

"""
/*
 * EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
 */
"""


def get_final_date() -> datetime:
    while True:
        try:
            print("Dame la fecha final:\n")
            day = input("Día: ")
            month = input("Mes: ")
            year = input("Año: ")
            hour = input("Hora: ")
            minute = input("Minuto: ")
            second = input("Segundo: ")

            date_str = day+"-"+month+"-"+year+" "+hour+":"+minute+":"+second
            date_daetime = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
            date_local = date_daetime.replace(tzinfo=ZoneInfo("Europe/Madrid"))

            # Convertir a UTC
            date_utc = date_local.astimezone(timezone.utc)
            return date_utc

        except ValueError:
            print("\nDatos no válidos\n")


def countdown(date: datetime) -> datetime:
    while True:
        current_date = datetime.now(timezone.utc)
        pending_time = date - current_date

        if pending_time.total_seconds() <= 0:
            print("Fecha alcanzada")
            break

        dias, horas, minutos, segundos = convert_seconds(
            int(pending_time.total_seconds()))
        os.system("clear")
        print(
            f"Faltan {dias} días, {horas} horas, {minutos} minutos, {segundos} segundos")

        sleep(1)


def convert_seconds(seconds: int) -> tuple[int]:
    days = seconds // 86400
    rest = seconds % 86400

    hours = rest // 3600
    rest = rest % 3600

    minutes = rest // 60
    seconds = rest % 60

    return (int(days), int(hours), int(minutes), int(seconds))


def main():

    fecha_final = get_final_date()
    hilo = Thread(target=countdown, args=(fecha_final,))
    hilo.daemon = False
    hilo.start()


if __name__ == "__main__":
    main()
