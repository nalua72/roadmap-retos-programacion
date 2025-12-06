from abc import ABC, abstractmethod

"""
Ejercicio:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Forma incorrecta
class PriceCalculator:
    def calculate(self, price, discount_type):
        if discount_type == "none":
            return price
        elif discount_type == "fixed":
            return price - 10
        elif discount_type == "percentage":
            return price * 0.9

# Forma correcta
class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class NoDiscount(Discount):
    def apply(self, price):
        return price

class FixedDiscount(Discount):
    def apply(self, price):
        return price - 10

class PercentageDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class PriceCalculator:
    def calculate(self, price, discount: Discount):
        return discount.apply(price)
    

""" 
* DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""

class Operations:
    @abstractmethod
    def operation(self, operator1, operator2):
        pass

class Add(Operations):
    def operation(self, operator1: float, operator2: float) -> float:
        return operator1 + operator2

class Substract(Operations):
    def operation(self, operator1: float, operator2: float) -> float:
        return operator1 - operator2
    
class Product(Operations):
    def operation(self, operator1: float, operator2: float) -> float:
        return operator1 * operator2
    
class Division(Operations):
    def operation(self, operator1: float, operator2: float) -> float:
        return operator1 / operator2
    
class Power(Operations):
    def operation(self, operator1: float, operator2: float) -> float:
        return operator1 ** operator2
    
class Calculator:
    def calculate(self, operator1: float, operator2: float, op: Operations):
        return op.operation(operator1, operator2)
    
def main():
    operador1 = 12
    operador2 = 24

    calculadora = Calculator ()

    print(f"La suma de {operador1} y {operador2} es: {calculadora.calculate(operador1, operador2, Add())}")
    print(f"La resta de {operador1} y {operador2} es: {calculadora.calculate(operador1, operador2, Substract())}")
    print(f"El producto de {operador1} y {operador2} es: {calculadora.calculate(operador1, operador2, Product())}")
    print(f"la division de {operador1} y {operador2} es: {calculadora.calculate(operador1, operador2, Division())}")
    print(f"la potencia de {operador1} y {operador2} es: {calculadora.calculate(operador1, operador2, Power())}")

if __name__ == "__main__":
    main()