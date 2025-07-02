""" MANEJO DE CADENAS """

texto: str = "esta es una cadena de ejemplo"

print(f"La longitud del texto '{texto}' es {len(texto)} caracteres") #Se puede imprimir y calcular la longitud

for caracter in texto:
    print(caracter)         #Es iterable

#Manejando mayusculas y minusculas
texto: str = "esta ES una cADEna de ejemplo"
print(texto.capitalize()) #Pone la primera letra en mayuscula y el rest en minusculas
print(texto.upper())    #Pone todo el texto en mayusuclas
print(texto.lower())    #Pone todo el texto en minusculas
print(texto.swapcase()) #Intercambia mayusucuals por minusculas

#Eliminando espacios en blanco
texto: str = "  Cadena con blancos en los extremos"
print(texto.strip())    #Elimina espacios en blanco al principio y final de la cadena
print(texto.lstrip())    #Elimina espacios en blanco al principio
print(texto.rstrip())    #Elimina espacios en blanco al final de la cadena

#Reemplaza una cadena de texto por otra
texto: str = "Hace mucho frio"
print(texto)
print(texto.replace("frio", "calor"))               
print("Hace mucho frio".replace("frio", "calor"))

#Separando texto usando espacios en blanco
texto: str = "Vamos a separar el texto usando los espacios"
palabras: list = texto.split()
print(texto)
print(palabras)
print("Otro ejemplo de separacion".split())

#Separando texto usando el caracter que queramos, en este caso la coma
texto: str = "uno,dos,tres,cuatro"
palabras: list = texto.split(",")
print(texto)
print(palabras)
print("Uno$mas$con$otro$separador".split("$"))

#Une elementos deuna lista en un string
lista: list = ["Vamos", "a", "probar", "join"]
texto: str = " ".join(lista)
print(lista)
print(texto)
print("-".join(["1", "2", "3", "4"]))

#Buscando subcadenas
texto: str = "Vamos a buscar subcadenas"
print(texto.find("s"))         #Posicion de la primera ocurrencia. Si no lo encuentra devuelve -1
print(texto.rfind("s"))         #Posicion de la ultima ocurrencia
print(texto.index("s"))         #Igual que find pero si no lo encuentra salta una excepcion
print(texto.startswith("Vamos")) #Devuelve True si el texto comienza con la cadena indicada
print(texto.endswith("Vamos")) #Devuelve True si el texto finaliza con la cadena indicada

#Comprobar tipo de cadena
print("looser".isalpha())       #True if all characters are letters
print("1972".isdigit())         #True if all characters are numbers
print("pasword1234".isalnum())  #True if all characters are letters or numbers
print("    ".isspace())         #True if all characters are whitespaces
print("PYTHON".isupper())       #True if all characters are capital letters
print("python".islower())       #True if all characters small letters

#Slicing
texto: str = "Texto a rebanar"
print(texto)
print(texto[:5])    #Desde el indice 0 al 4
print(texto[3:10])   #Desde el indice 3 al 9
print(texto[11:])   #Desde el indice 11 al final
print(texto[-1])   #Ultimo caracter
print(texto[-5:])   #Ultimos 5 caracteres
print(texto[::2])   #Cada 2 caracteres
print(texto[::-1]) #Pcadena del reves

#Managing types
numero_string = "1234"
print(numero_string, type(numero_string))
numero_int = int(numero_string)
print(numero_int, type(numero_int))
numero_int += 250
print(numero_int, type(numero_int))
numero_string = str(numero_int)
print(numero_string, type(numero_string))
numero_float = numero_int * 2.5
print(numero_float, type(numero_float))
numero_string = str(numero_float)
print(numero_string, type(numero_string))

""" EXTRA """

def ispalindroma(cadena: str) -> bool:
    """
    Checks if a word is palymdrome.
    
    Args:
    cadena (string): word to check
    
    Returns:
    bool: DTrue if word is palymdrome
    """
    #Checks if a word is palyndrome
    if cadena == cadena[::-1]:
        return True
    return False

def isanagram(cadena1: str, cadena2: str) -> bool:
    """
    Check if 2 words are anagrams.
    
    Args:
    word1 (string): word to check if is anagram of another word
    word2 (string): word to check if is anagram of another word
    
    Returns:
    bool: True if one word is anagram of the other
    """
    #Checks if 2 words are anagrams
    if sorted(cadena1) == sorted(cadena2):
        return True
    return False

def isogram(cadena: str) -> bool:
    """
    Check if one word is isogram
    
    Args:
    cadena (string): DWord to check if it is isogram
    
    Returns:
    bool: True if the word is isogram
    """
    alphabet: dict = {}

    #Creates a dictonary KEY:each letter of the word Value:how many times appears in the word
    for l in cadena:
        if l in alphabet:
            alphabet[l] += 1
            continue
        alphabet[l] = 1
    #Converts the list of values into a set to remove duplicates. If the length of the set is 1 
    #then the word is isogram
    return (len(set(alphabet.values())) == 1)

def check_words(word1: str, word2: str):
    """
    Check if 2 words are palyndormes, isograms and anagrams of each other
    
    Args:
    word1 (string): First word to check
    word2 (string): Second word to check
    """

    #Check if first word is palyndrome
    if ispalindroma(word1):
        print(f"{word1} es palindroma")
    else:
        print(f"{word1} no es palindroma")

    #Check if second word is palyndrome
    if ispalindroma(word2):
        print(f"{word2} es palindroma")
    else:
        print(f"{word2} no es palindroma")

    #Check if first word is isogram
    if isogram(word1):
        print(f"{word1} es isograma")
    else:
        print(f"{word1} no es isograma")
    
    #Check if second word is isogram
    if isogram(word2):
        print(f"{word2} es isograma")
    else:
        print(f"{word2} no es isograma")

    #Check if first word and second words are anagrams of each other
    if isanagram(word1, word2):
        print(f"{word1} y {word2} son anagramas")
    else:
        print(f"{word1} y {word2} no son anagramas")


def main():
    """
    Main function
    """
    print("#"*100)
    print("\n")

    #Calling the functions
    check_words("radar", "pythonpythonpythonpython")
    check_words("amor", "roma")

if __name__ == "__main__":
    main()
