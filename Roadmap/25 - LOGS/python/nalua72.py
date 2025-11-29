import logging
import time


""" 
Ejercicio
"""

# Configurar el logging
# logging.basicConfig(level=logging.DEBUG)  # Nivel mínimo: DEBUG

# logging.debug("Mensaje de depuración")
# logging.info("Mensaje informativo")
# logging.warning("Cuidado! Advertencia")
# logging.error("Ocurrió un error")
# logging.critical("Error crítico!")


""" logging.basicConfig(
    filename="mi_programa.log",
    level=logging.INFO,  # se guardan INFO y niveles superiores
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Inicio del programa")
logging.warning("Algo puede ir mal")
logging.error("Error al procesar datos")
logging.debug("Esto es una prueba") """


""" 
Extra
"""

logging.basicConfig(
        filename="tasks_app.log",
        level=logging.DEBUG,  # se guardan DEBUG y niveles superiores
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_execution_time(func):
    """Decora una función para medir cuánto tarda en ejecutarse."""
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        result = func(*args, **kwargs)
        final = time.perf_counter()
        duracion = final - inicio
        logging.debug(f"Tiempo de ejecución de {func.__name__}: {duracion:.6f} s")
        return result
    return wrapper

class Tasks():
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            logging.info("Inicio del programa")
            cls._instance = super().__new__(cls)
            cls._instance._tasks_list = []
        return cls._instance


    @log_execution_time
    def add_task(self, name: str, description: str) -> None:
        self._tasks_list.append({"nombre": name, "descripcion": description})
        logging.info(f"Tarea: {name}, añadida")
       

    @log_execution_time
    def list_task(self) -> None:
        if self._tasks_list:
            logging.info("Mostrando la lista de tareas")
            for task in self._tasks_list:
                print(task)
        else:
            logging.warning("Intentando mostrar una lista de tareas vacia")


    @log_execution_time
    def del_task(self, name: str) -> None:
        if not self._tasks_list:
            logging.warning("Intentando borrar tareas cuando la lista está vacía")
            return
        
        for i, task in enumerate(self._tasks_list):
            if task['nombre'] == name:
                removed = self._tasks_list.pop(i)
                logging.info(f"Borrada tarea: {removed['nombre']}")
                print(f"Borrada tarea: {removed['nombre']}")
                return
        
        logging.warning(f"La tarea '{name}' no existe")

    def _print_time(self, start_time, end_time):
        duracion = (end_time - start_time)
        logging.debug(f"La tarea ha durado {duracion:.6f} segundos")


def main():
    tasks = Tasks()

    tasks.add_task("tarea1", "Descripcion tarea1")
    tasks.add_task("tarea2", "Descripcion tarea2")
    tasks.add_task("tarea3", "Descripcion tarea3")
    tasks.list_task()
    tasks.del_task("tarea2")
    tasks.list_task()
    tasks.del_task("tarea2")
    tasks.del_task("tarea1")
    tasks.del_task("tarea3")
    tasks.list_task()
    tasks.del_task("tarea2")

if __name__ == "__main__":
    main()