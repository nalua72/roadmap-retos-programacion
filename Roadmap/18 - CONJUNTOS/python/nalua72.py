""" EJERCICIO """

conjunto = [1, 2, 3, 4, 5]
print(f"Conjunto: {conjunto}")

# Añade un elemento al final.

conjunto.append(6)
print(f"Añado un elemento al final: {conjunto}")

# Añade un elemento al principio.
conjunto.insert(0,0)
print(f"Añado un elemento al principio: {conjunto}")

# Añade varios elementos en bloque al final.

conjunto.extend([7, 8, 9])
print(f"Añado varios elementos en bloque al final: {conjunto}")

# Añade varios elementos en bloque en una posición concreta.

conjunto[4:4] = [0, 0 ,0]
print(f"Añado varios elementos en una posición concreta: {conjunto}")

# Elimina un elemento en una posición concreta.

conjunto.pop(4)
print(f"Elimina un elemento en una posición concreta: {conjunto}")

# Actualiza el valor de un elemento en una posición concreta.

conjunto[4] = 9
print(f"Actualiza el valor de un elemento en una posición concreta: {conjunto}")

# Comprueba si un elemento está en un conjunto.

print(f"omprueba si un elemento está en un conjunto: {3 in conjunto}")
    
# Elimina todo el contenido del conjunto.

print(f"Elimina el contenido del conjunto: {conjunto.clear()}")

""" EXTRA """

# Muestra ejemplos de las siguientes operaciones con conjuntos:

conjunto_1 = {1, 2, 3}
conjunto_2 = {3, 4, 5, 6}

print(f"Conjunto 1: {conjunto_1}\nConjunto 2: {conjunto_2}")

# Unión.

print(f"Unión de conjuntos {conjunto_1 | conjunto_2}")

# Intersección.

print(f"Intersección de conjuntos {conjunto_1 & conjunto_2}")

# Diferencia.

print(f"Diferencia de conjuntos {conjunto_1 - conjunto_2}")

# Diferencia simétrica.

print(f"Diferencia simétrica de conjuntos {conjunto_1 ^ conjunto_2}")
