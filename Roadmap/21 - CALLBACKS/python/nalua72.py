import time
import random
import threading


""" Ejemplo de callback """

def hello_callback(user):
    print(f"Hola {user}")

def hello_process(user, callback):
    print(f"Llamo a la funcion callback")
    callback(user)
    print(f"La funcion callback ha fimalizado")

hello_process("Jose", hello_callback)


""" EXTRA """

def pedido_confirmado(dish):
    print(f"Pedido {dish} confirmado")

def pedido_listo(dish):
    print(f"Pedido {dish} listo")

def pedido_entregado(dish):
    print(f"Pedido {dish} entregado")


def procesar_pedido(plato, call_confirmado, call_listo, call_entregado):
    call_confirmado(plato)
    time.sleep(random.randint(1, 10))
    call_listo(plato)
    time.sleep(random.randint(1, 10))
    call_entregado(plato)

def main():
    pedidos = ["numero1", "numero2", "numero3"]
    tasks = []

    for pedido in pedidos:
        task = threading.Thread(target=procesar_pedido, args=(pedido, pedido_confirmado, pedido_listo, pedido_entregado))
        task.start()
        tasks.append(task)

    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()