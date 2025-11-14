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

def pedido(plato, call_confirmado, call_listo, call_entregado):
    def flujo_pedido():
        call_confirmado(plato)
        time.sleep(random.randint(1, 10))
        call_listo(plato)
        time.sleep(random.randint(1, 10))
        call_entregado(plato)

    threading.Thread(target=flujo_pedido).start()

def main():

    pedido("numero1", pedido_confirmado, pedido_listo, pedido_entregado)
    pedido("numero2", pedido_confirmado, pedido_listo, pedido_entregado)
    pedido("numero3", pedido_confirmado, pedido_listo, pedido_entregado)


if __name__ == "__main__":
    main()