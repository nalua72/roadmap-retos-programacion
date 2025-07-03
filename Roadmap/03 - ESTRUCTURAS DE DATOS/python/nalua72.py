""" Extructura de datos """

#Tuplas. Conjunto de datos iterables e inmutables

ejemplo1_tupla = (1, 2, 3, 4, 5) #Crea tupla
print(ejemplo1_tupla)           #Imprime tupla
print(ejemplo1_tupla[3])        #Seleciona elemento

ejemplo2_tupla = ("norte", "sur", "este", "oeste")
print(ejemplo2_tupla)
print(ejemplo2_tupla[0])

#Listas. Conjunto de datos iterables y mutables

ejemplo1_lista = [103, 102, 105, 101, 104] #Crea lista
print(ejemplo1_lista)
ejemplo1_lista.sort()               #Ordena lista
print(ejemplo1_lista)

compra_lista = ["leche", "pan", "huevos", "tomates", "lechuga"]
for alimento in compra_lista:
    print(alimento)           #Imprime lista
print(f"la lista de la compra tiene {len(compra_lista)} elementos") #Calcula longitud lista
compra_lista.append("helados") #Añade elemento
print(compra_lista)
compra_lista.remove("pan") #Elimina elemento
print(compra_lista)

#Diccionarios. Almacena pares de valores KEY/VALUE
familia ={
    "padre": "Jose",
    "madre": "Isabel",
    "abuelom": "Juan",
    "abuelam": "Maria"
}                       #Creacion de un diccionario
print(familia)
print(familia["padre"]) #Seleecion por clave
familia["abuelop"] = "Manuel" #Añade campo
print(familia)
familia["abuelap"] = "Maria"
print(familia)
familia["abuelap"] = "Carmen" #Modifica Campo
print(familia)

#Sets. almacena elementos no rpetidos

mlista = [23, 56, 78, 56, 23, 68, 99, 68]
print(mlista)
mset = set(mlista) #Crea un set a partir de una lista
print(mset)
mset.add(34) #Añade un elemento
print(mset)
mset.remove(78) #Elimina un elemento
print(mset)


""" Ejercicio extra """

def print_menu() -> str:
    """
    Prints on console a simple menu
    
    Returns:
    type: String (Asks the user to select an option from the menu)
    """
    print("")
    print("\t", "*"*25)
    print("\t1- Listar agenda")
    print("\t2- Buscar usuario")
    print("\t3- Insertar usuario")
    print("\t4- Actualizar usuario")
    print("\t5- Borrar usuario")
    print("\t6- Salir")
    print("\t", "*"*25)
    print("")
    return input("Por favor escoge una opcion: ")


def get_user_info():
    """
    Gets user Name and phone number
        
    Returns:
    type: No returns
    """
    name = str(input("Nombre usuario: "))
    while True:
        phone_number = input("Telefono de usuario: ")
        if phone_number.isdigit() and len(phone_number) < 12:
            return {"name" : name, "phone_number": phone_number}
        print("El numero de telefono debe tener un maximo de 11 digitos")

def display_user(user):
    """
    Displays on console the user information
    
    Returns:
    No return value
    """
    print(f"\nNombre usuario: {user['name']}, telefono del usuario: {user['phone_number']}")

def list_users(userlist: list[dict]):
    """
    Gets the users informafion from a list and displays them on console
    
    Args:
    userlist (type: list[dict]): A list of dictioneries. Each dictionary contents the user details
        
    Returns:
    No return value
    """
    if len(userlist) > 0:
        print("Listado de usuarios:")
        for user in userlist:
            display_user(user)
    else:
        print("Agenda vacia")

def insert_user(userlist: list[dict]):
    """
    Inserts a new user in the agenda if it doesn't exit
    
    Args:
    userlist (type: list[dict]): A list of dictioneries. Each dictionary contents the user details
    """
    user = get_user_info()
    if not any(user['name'] in dict.values() for dict in userlist):
        userlist.append(user)
    else:
        print(f"Usuario {user['name']} ya existe")

def update_user(userlist: list[dict]) -> None:
    """
    Updates an existing user details
    
    Args:
    userlist (type: list[dict]): A list of dictioneries. Each dictionary contents the user details
    
    Returns:
    (type: list[dict]): A list of dictioneries. Each dictionary contents the user details
    """
    username = input("Introduce el usuario a actualizar: ")
    for user in userlist:
        if user['name'] == username:
            print(f"Actualizando el usuario: {username}")
            user.update(get_user_info())
            return None
    print(f"El usuario {username} no existe")
    return None

def delete_user(userlist: list[dict]):
    """
    Deletes a user from the agenda if it exits
    
    Args:
    userlist (type: list[dict]): A list of dictioneries. Each dictionary contents the user details
    
    Returns:
    (type: list[dict]): A list of dictioneries. Each dictionary contents the user details
    """
    username = input("Introduce el usuario a borrar: ")
    if any(username in dict.values() for dict in userlist):
        print(f"Borrando usuario: {username}")
        for user in userlist:
            if user['name'] == username:
                userlist.remove(user)
                break
    else:
        print(f"El usuario {username} no existe")

def search_user(userlist: list[dict]) -> None:
    """
    Search for an user in the agenda and if exits, displays it
    
    Args:
    userlist (type: list[dict]): A list of dictioneries. Each dictionary contents the user details
    
    Returns:
    (type: None):
    """
    username = input("Introduce el usuario a buscar: ")
    for user in userlist:
        if user['name'] == username:
            display_user(user)
            return None
    print(f"El usuario {username} no existe")
    return None

def main():
    """
    Main function call. 

    """
    agenda = []
    while True:
        option = print_menu()
        match option:
            case "1":
                list_users(agenda)
            case "2":
                search_user(agenda)
            case "3":
                insert_user(agenda)
            case "4":
                agenda = update_user(agenda)
            case "5":
                delete_user(agenda)
            case "6":
                print("Saliendo")
                break
            case _:
                print("Escoge una opción del 1 al 6")

if __name__ == "__main__":
    main()
