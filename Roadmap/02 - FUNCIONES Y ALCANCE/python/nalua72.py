""" 
TIPOS DE FUNCIONES 
"""

#Sin parametors ni retorno
def sin_retorno():
    print("Aprendiendo python")

sin_retorno()

#Sin parametros con retorno
def con_retorno() -> str:
    return "Aqui sigo"

print(con_retorno())

#Sin parametros varios retornos
def con_varios_retornos():
    return "Estoy", "feliz"

verb, estado = con_varios_retornos()
print(f"{verb} {estado}")

#Sin retorno y un parametro
def sin_retorno_parametro(param: str):
    print(f"Hola, {param}")

sin_retorno_parametro("PYTHON")

#Sin retorno con dos parametros. Uno con valor por defecto
def sin_retorno_varios_parametros(param1: str, param2: str = "Moure"):
    print(f"Hola {param1} {param2}")

sin_retorno_varios_parametros("Brais")
sin_retorno_varios_parametros("Juan", "Valiente")

#Con retorno un parametro
def con_retorno_parametro(param: str) -> str:
    return f"Probando {param}"

print(con_retorno_parametro("Python"))

#Con retorno varios parametros. Uno con valor por defecto
def con_retorno_varios_parametros(param1: str, param2: str = "calor") -> str:
    return f"En {param1} hace mucho {param2}"

print(con_retorno_varios_parametros("Valladolid"))
print(con_retorno_varios_parametros("Burgos", "frio"))

#Sin retorno con un numero variable de parametros

def sin_retorno_nvariable_parametros(*params: str):
    for param in params:
        print(param)

sin_retorno_nvariable_parametros("Ejemplo", "llamada", "numero variable", "parametros")

#Sin retorno con un diccionario como parametro
def sin_retorno_dictionario(**dicc):
    for clave, valor in dicc.items():
        print(f"{clave}: {valor}")

sin_retorno_dictionario(
    Calle="Melancolia",
    Barrio="Alegria",
    Numero=7
)

""" Llamadas a funciones """

#Llamadas a funciones del sistema

cadena = "Esto es una texto"

print(f"la variable {cadena} es de tipo:", type(cadena), "y tiene una longitud:", len(cadena))

#Crear funcion dentro de una funcion
def comparar_tres_numeros(num1: int, num2: int, num3: int) -> int:
    def comparar_dos_numeros(a: int, b: int) -> int:
        if a > b:
            return a
        return b
    return comparar_dos_numeros(num1, comparar_dos_numeros(num2, num3))

print(comparar_tres_numeros(9, 16, 11))

#Variable local y variable global

variable_global = "Global"

def imprimir_variables():
    variable_local = "Local"
    print(f"{variable_global}, {variable_local}")

imprimir_variables()
print(variable_global) #Si se intenta imprimir la variable local, da una excepcion

""" 
DiFICULTAD EXTRA 
"""

def func_extra(cadena1: str, cadena2: str) -> int:
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            contador += 1
    return contador


print(func_extra("multiplo de 3", "multiplo de 5"))