def factorial(n: int) -> int:
    """
    Calculates the factorial of a number
    
    Args:
    n1 (int): Number of whic factorial is going to be calculated
    
    Returns:
    int: Factorial of the number n
    """
   #Number can't be negative
    if n < 0:
        return 0
    
    # n! = 1. Point of exit of the recursive function
    if n == 0:
        return 1
    
    return n*factorial(n-1)

def fibonacci(pos: int) -> int:
    """
    Calculates the value of the fibonacci serie in the provided position
    
    Args:
    pos (int): The position in the Fibonacci serie we want the value for
    
    Returns:
    int: Fibonacci value
    """

    #Position can´t be 0 or negative
    if pos <= 0:
        return 0
    
    # fibonacci(1) = fibonacci(2) = 1. Point of exit of the recursive function
    if pos in (1,2):
        return 1
    
    return fibonacci(pos-1) + fibonacci(pos-2)

def main():
    """
    Main function
    """
    numero: int = 10

    print(f"El factorial de {numero} es:", factorial(numero))
    print(f"El valor de la serie de fibonacci en la posicion {numero} es:", fibonacci(numero))

if __name__ == "__main__":
    main()

