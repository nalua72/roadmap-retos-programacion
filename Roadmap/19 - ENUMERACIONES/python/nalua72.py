""" Ejercicio """

from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def dia(index: int) -> None:
    print(DiaSemana(index).name)

dia(3) # Miercoles
dia(7) # Domingo


""" EXTRA """

class Estado(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4

class Pedido():

    estado = Estado.PENDIENTE

    def __init__(self, id):
        self.id = id

    def enviado(self):
        if self.estado.name == "PENDIENTE":
            print(f"Pedido {self.id}: enviado")
            self.estado = Estado.ENVIADO
        else:
            print(f"El pedido {self.id}, no se ha podido enviar porque esta en estado: {self.estado.name}")
    
    def entregado(self):
        if self.estado.name == "ENVIADO":
            print(f"Pedido {self.id}: entregado")
            self.estado = Estado.ENTREGADO
        else:
            print(f"El pedido {self.id}, no se ha podido enviar porque esta en estado: {self.estado.name}")

    def cancelado(self):
        if self.estado.name == "PENDIENTE":
            print(f"Pedido {self.id}: cancelado")
            self.estado = Estado.CANCELADO
        else:
            print(f"El pedido {self.id}, no se ha podido enviar porque está en estado: {self.estado.name}")
    
    def __str__(self):
        return(f"El pedido {self.id}, está en estado: {self.estado.name}")

def main():
    
    #Inicializa los pedidos
    pedido1 = Pedido(101)
    pedido2 = Pedido(102)
    pedido3 = Pedido(103)

    print(pedido1)
    print(pedido2)
    print(pedido3)

    #Modifico los pedidos
    pedido1.entregado()
    pedido2.enviado()
    pedido3.cancelado()

    print(pedido1)
    print(pedido2)
    print(pedido3)

     #Modifico los pedidos
    pedido1.enviado()
    pedido2.entregado()
    pedido3.enviado()

    print(pedido1)
    print(pedido2)
    print(pedido3)   

if __name__ == "__main__":
    main()
