import asyncio
from datetime import datetime

async def task(name, seconds):
# Definición de una función asíncrona que simula una tarea con duración variable

    print(f"Tarea {name} con duracion {seconds} segundos empieza a las {datetime.now()}")
    await asyncio.sleep(seconds)
    # Mensaje indicando que la tarea ha terminado
    print(f"Tarea {name} con duracion {seconds} segundos termina a las {datetime.now()}")

# Ejecuta una tarea de prueba de forma asíncrona
asyncio.run(task("PRUEBA", 4))

""" EXTRA """

# Definimos una función principal asíncrona que ejecuta varias tareas en paralelo
async def main():
    # Ejecuta las tareas C, B y A simultáneamente usando asyncio.gather
    await asyncio.gather(
        task("C", 3),
        task("B", 2),
        task("A", 1)
    )
    # Ejecuta la tarea D después de que las anteriores hayan terminado
    await task("D", 1)

# Punto de entrada del script: ejecuta la función main usando asyncio.run
if __name__ == "__main__":
    asyncio.run(main())
    