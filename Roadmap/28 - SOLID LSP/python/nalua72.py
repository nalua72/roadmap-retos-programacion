from abc import ABC, abstractmethod


"""  
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

#Forma incorrecta
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor
        self._alto = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        self._alto = valor
        self._ancho = valor


#Forma correcta
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    

def set_dimensions(rect: Rectangulo):
    rect.ancho = 10
    rect.alto = 5
    print(rect.area())

rect1 = Rectangulo(10,5)
rect2 = Cuadrado(10)

set_dimensions(rect1)

"""  
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
"""


class Vehicle(ABC):

    @abstractmethod
    def accelerate(self):
        pass


    @abstractmethod            
    def brake(self):
        pass


class Car(Vehicle):

    def accelerate(self):
        print("Puedo acelerar hasta 120km/h")


    def brake(self):
        print("Frenando el coche")


class Truck(Vehicle):

    def accelerate(self):
        print("Puedo acelerar hasta 90Km/h")
        
        
    def brake(self):
        print("Frenando el camion")


class Bike(Vehicle):

    def accelerate(self):
        print("Puedo acelerar hasta 60Km/h")

    def brake(self):
        print("Frenando la bicicleta")
        

def vehicle_test(v: Vehicle):
    v.accelerate()
    v.brake()

def main():
    coche = Car()
    camion = Truck()
    bicicleta = Bike()

    vehicle_test(coche)
    vehicle_test(camion)
    vehicle_test(bicicleta)


if __name__ == "__main__":
    main()
