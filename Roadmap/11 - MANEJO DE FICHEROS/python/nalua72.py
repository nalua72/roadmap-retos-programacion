import pathlib
"""
This script demonstrates basic file handling operations in Python, including writing, reading, appending, and deleting a text file.
Operations performed:
1. Creates and writes initial content to 'nalua72.txt' using write() and writelines().
2. Reads and prints the entire file content.
3. Reads and prints each line from the file, stripping newline characters.
4. Appends a new line to the file.
5. Reads and prints all lines again, including the newly appended line.
6. Checks if the file exists and deletes it, printing a confirmation message.
Modules used:
- pathlib: For file existence check and deletion.
"""

with open("nalua72.txt", "w") as f:
    f.write("Jose Manuel Rodriguez\n")
    f.writelines(["53 años\n", "Lenguaje favorito: Python\n"])

with open("nalua72.txt", "r") as f:
    contenido = f.read()
    print(contenido)
    
with open("nalua72.txt", "r") as f:
    lineas = f.readlines()
    for linea in lineas:
        print(linea.strip())

with open("nalua72.txt", "a") as f:
    f.write("Nuevo lenguaje: Lua\n")

with open("nalua72.txt", "r") as f:
    liners = f.readlines()
    for liner in liners:
        print(liner.strip())

file = pathlib.Path("nalua72.txt")
if file.exists():
    file.unlink()
    print("El archivo ha sido eliminado.")

""" EXTRA """

def print_menu() -> str:
    """
    Prints on console a simple menu
    
    Returns:
    type: String (Asks the user to select an option from the menu)
    """
    print("")
    print("\t", "*"*25)
    print("\t1- Añadir producto")
    print("\t2- Consultar producto")
    print("\t3- Consultar todo los productos")
    print("\t4- Actualizar producto")
    print("\t5- Eliminar producto")
    print("\t6- Ventas totales")
    print("\t7- Ventas por producto")
    print("\t8 Salir")
    print("\t", "*"*25)
    print("")
    return input("Por favor escoge una opcion: ")

def add_product():
    """
    Function to add a product
    """
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad_vendida = input("Ingrese la cantidad vendida: ")
    precio = input("Ingrese el precio unitario: ")

    with open("nalua72.txt", "a") as f:
        f.write(f"{nombre_producto}, {cantidad_vendida}, {precio}\n")


def consult_product():
    """
    Function to consult a product
    """
    consulta_producto = input("Ingrese el nombre del producto a consultar: ")
    with open("nalua72.txt", "r") as f:
        liners = f.readlines()
        for liner in liners:
            if [prod.strip() for prod in liner.split(",")][0] == consulta_producto:
                print(liner.strip())
                

def consult_products():
    """
    Function to consult all products
    """
    with open("nalua72.txt", "r") as f:
        liners = f.readlines()
        for liner in liners:
            print(liner.strip())

def update_product():
    """
    Function to update a product
    """
    actualizar_producto = input("Ingrese el nombre del producto a actualizar: ")
    actualizar_cantidad = input("Ingrese la cantidad del producto a actualizar: ")
    actualizar_precio = input("Ingrese el precio del producto a actualizar: ")

    with open("nalua72.txt", "r") as f:
        liners = f.readlines()

    with open("nalua72.txt", "w") as f:
        for liner in liners:
            if [prod.strip() for prod in liner.split(",")][0] == actualizar_producto:
                f.writelines(f"{actualizar_producto}, {actualizar_cantidad}, {actualizar_precio}\n")
            else:
                f.writelines(f"{liner}")


def delete_product():
    """
    Function to delete a product
    """ 
    borrar_producto = input("Ingrese el nombre del producto a borrar: ")
    with open("nalua72.txt", "r") as f:
        liners = f.readlines()

    with open("nalua72.txt", "w") as f:
        for liner in liners:
            if [prod.strip() for prod in liner.split(",")][0] != borrar_producto:
                f.writelines(f"{liner}")


def ventas_totales():    
    """
    Function to calculate total sales
    """ 
    total_ventas = 0.0
    with open("nalua72.txt", "r") as f:
        liners = f.readlines()
        for liner in liners:
            partes = [prod.strip() for prod in liner.split(",")]
            if len(partes) == 3:
                try:
                    cantidad = float(partes[1])
                    precio = float(partes[2])
                    total_ventas += cantidad * precio
                except ValueError:
                    print(f"Error al convertir cantidad o precio a número en la línea: {liner.strip()}")
    print(f"El total de ventas es: {total_ventas}") 


def ventas_por_producto():
    """
    Function to calculate sales by product
    """
    ventas_por_producto = 0.0

    ventas_producto = input("Ingrese el nombre del producto a calcular sus ventas: ")
    with open("nalua72.txt", "r") as f:
        liners = f.readlines()
        for liner in liners:
            if [prod.strip() for prod in liner.split(",")][0] == ventas_producto:
                partes = [prod.strip() for prod in liner.split(",")]
                try:
                    cantidad = float(partes[1])
                    precio = float(partes[2])
                    ventas_por_producto += cantidad * precio
                except ValueError:
                    print(f"Error al convertir cantidad o precio a número en la línea: {liner.strip()}")
    print(f"El total de ventas del producto {ventas_producto} es: {ventas_por_producto}")


def exit_program():
    """
    Function to exit the program
    """
    file = pathlib.Path("nalua72.txt")
    if file.exists():
        file.unlink()
        print("El archivo ha sido eliminado.")


def main():
    """
    Main function to run the menu loop
    """
    opcion = ""
    while opcion != "8":
        opcion = print_menu()
        if opcion == "1":
            print("Has seleccionado la opción 1: Añadir producto")
            add_product()
        elif opcion == "2":
            print("Has seleccionado la opción 2: Consultar producto")
            consult_product()
        elif opcion == "3":
            print("Has seleccionado la opción 3: Consultar todos los productos")
            consult_products()    
        elif opcion == "4":
            print("Has seleccionado la opción 4: Actualizar producto")
            update_product()
        elif opcion == "5":
            print("Has seleccionado la opción 5: Eliminar producto")
            delete_product()
        elif opcion == "6":
            print("Has seleccionado la opción 6: Ventas totales")
            ventas_totales()
        elif opcion == "7":
            print("Has seleccionado la opción 7: Ventas por producto")
            ventas_por_producto()
        elif opcion == "8":
            print("Saliendo del programa...")
            exit_program()
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
