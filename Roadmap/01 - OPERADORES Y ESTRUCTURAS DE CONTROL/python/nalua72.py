""" OPERADORES """

num1 = 10
num2 = 7

# Aritmeticos
print(f"numero1: {num1} y numero2: {num2}")
print(f"Suma {num1} + {num2}: {num1+num2}")
print(f"Resta {num1} - {num2}: {num1-num2}")
print(f"Multiplicacion: {num1} * {num2}: {num1*num2}")
print(f"Exponente {num1} ** {num2}: {num1**num2}")
print(f"Division {num1} / {num2}: {num1/num2}")
print(f"Division entera {num1} // {num2}: {num1//num2}")
print(f"Modulo {num1} % {num2}: {num1%num2}")

num3 = 10
print(f"Toma un numero: {num3}")
num3 += 1
print(f"Sumale 1: {num3}")
num3 -= 2
print(f"Restale 2: {num3}")
num3 *= 3
print(f"Multiplicalo por 3: {num3}")
num3 /= 4
print(f"Dividelo por 4: {num3}")
num3 **= 5
print(f"Elevalo a la 5 potencia: {num3}")
num3 //= 6
print(f"Halla su division entera por 6: {num3}")
num3 %= 7
print(f"Calcula su modulo 7: {num3}")

#Comparacion
print(f"{num1} es igual a {num2}: {num1 == num2}")
print(f"{num1} es distinto a {num2}: {num1 != num2}")
print(f"{num1} es mayor o igual a {num2}: {num1 >= num2}")
print(f"{num1} es menor o igual a {num2}: {num1 <= num2}")
print(f"{num1} es mayor a {num2}: {num1 > num2}")
print(f"{num1} es menor a {num2}: {num1 <= num2}")

#Logicos
print(f"y (and &&): {num1} + {num2} == 17 y {num1} - {num2} == 3: \
      {num1 + num2 == 17 and num1 - num2 == 3}")
print(f"or (or ||): {num1} + {num2} == 17 and {num1} - {num2} == 3: \
      {num1 + num2 == 17 or num1 - num2 == 4}")
print(f"not (!): not {num1} + {num2} == 14: {not num1+ num2 == 14}")

# Operadores de bit (Este bloque no se me ocurrio)
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

""" CONTROL """

#Si entonces sino
if num1 == num2:
    print(f"Los numeros {num1} y {num2} son iguales")
elif num1 >= num2:
    print(f"El numero {num1} es mayor que {num2}")
else:
    print(f"el numero {num1} es mas pequeño que el numero {num2}")

#For (Escribir los 10 primeros digitos)
for i in range(0,10):
    print(i)

#While (Escribir los 10 primeros digitos)
i = 0
while i < 10:
    print(i)
    i += 1

#Excepciones
try:
    print(f"{num1}/{num2}: {num1/num2}")
except:
    print("Algo ha ido mal")
else:
    print("Este bloque se ejecuta si todo ha ido bien")
finally:
    print("este bloque se ejecuta siempre")

""" DIFICULTAD EXTRA """

# Crea una lista de numeros omprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
lista_numeros = [x for x in range(10, 56) if x % 2 == 0 and x != 16 and x % 3 != 0]

# Imprime la lista
print(lista_numeros)
