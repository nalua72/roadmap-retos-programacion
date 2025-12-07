from abc import ABC, abstractmethod


"""  
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""


#Forma incorrecta
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Human(Worker):
    def work(self):
        print("El humano trabaja")

    def eat(self):
        print("El humano come")

    def sleep(self):
        print("El humano duerme")


class Robot(Worker):
    def work(self):
        print("El robot trabaja")

    def eat(self):
        raise NotImplementedError("Un robot no come")

    def sleep(self):
        raise NotImplementedError("Un robot no duerme")

#Forma correcta
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass


class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("El humano trabaja")

    def eat(self):
        print("El humano come")

    def sleep(self):
        print("El humano duerme")


class Robot(Workable):
    def work(self):
        print("El robot trabaja")


"""  
 DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
"""

class BlackAndWhite(ABC):
    @abstractmethod
    def print_black_and_white(self):
        pass

class Colour(ABC):
    @abstractmethod
    def print_colour(self):
        pass


class Scan(ABC):
    @abstractmethod
    def scan(self):
        pass


class Fax(ABC):
    @abstractmethod
    def send_fax(self):
        pass


class BWPrinter(BlackAndWhite):
    def print_black_and_white(self):
        print("Soy una impresora de blanco y negro y estoy imprimiendo en blanco y negro")


class CPrinter(Colour):
    def print_colour(self):
        print("Soy uuna impresora de color y estoy imprimiendo en color")


class MPrinter(BlackAndWhite, Colour, Scan, Fax):
    def print_black_and_white(self):
        print("Soy una impresora multifuncion y estoy imprimiendo en blanco y negro")


    def print_colour(self):
        print("Soy una impresora multifuncion y estoy imprimiendo en color")


    def scan(self):
        print("Soy una impresora multifuncion y estoy escaneando")


    def send_fax(self):
        print("Soy una impresora multifuncion y estoy enviando un fax")


def main():
    impresora_bn = BWPrinter()
    impresora_color = CPrinter()
    impresora_multifuncion = MPrinter()

    impresora_bn.print_black_and_white()
    impresora_color.print_colour()
    impresora_multifuncion.print_black_and_white()
    impresora_multifuncion.print_colour()
    impresora_multifuncion.scan()
    impresora_multifuncion.send_fax()


if __name__ == "__main__":
    main()