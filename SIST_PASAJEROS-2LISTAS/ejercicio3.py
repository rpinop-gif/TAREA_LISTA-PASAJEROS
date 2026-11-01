#ORDENAR UNA LISTA (BUBBLE SORT)
#Implementar el algoritmo de ordenamiento burbuja sobre una lista. Luego comparar con list.sort().

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# una lista de números desordenada

# Proceso — qué hago con eso
# recorrer varias veces intercambiando pares consecutivos

# Salida — qué debo mostrar
# la lista ordenada

#2 "BSOQUEJO A MANO:"
#[5, 2, 8, 1, 9]

# Vuelta 1:
#   5>2 → swap → [2, 5, 8, 1, 9]
#   5<8 → nada
#   8>1 → swap → [2, 5, 1, 8, 9]
#   8<9 → nada
# Vuelta 2:
#   2<5 → nada
#   5>1 → swap → [2, 1, 5, 8, 9]
#   5<8, 8<9 → nada
# Vuelta 3:
#   2>1 → swap → [1, 2, 5, 8, 9]


#3 "DESCUBRIR EL PATRON:"
#El bubble sort funciona comparando parejas consecutivas y las intercambia si están 
# desordenadas. Después de cada vuelta, el más grande queda al final (por eso «burbuja»).

#Es lento (O(n²)) — solo se enseña por su claridad conceptual.
#  En la vida real siempre usa lista.sort().


#4 "ESCRIBIR EL CODIGO:"
def bubble_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for vuelta in range(n - 1):
        # Bandera para optimizar: si en una vuelta no hubo swaps, ya está ordenado
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if arr[i] > arr[i + 1]:
                # Intercambio en una línea
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hubo_swap = True
        if not hubo_swap:
            break
    return arr


# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión
ordenada = bubble_sort(notas)
print(ordenada)                            # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]                           # copia para no romper el original
copia.sort()
print(copia)                               # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)                               # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)                            # ['a', 'el', 'python', 'código']


#Ahora tú
#Implementa selection sort: en cada vuelta busca el mínimo del resto y lo coloca al inicio.
def selection_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for i in range(n - 1):
        # Suponemos que el mínimo está en la posición actual
        min_idx = i
        # Buscamos el mínimo en el resto de la lista (desde i + 1 hasta el final)
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el mínimo encontrado con el elemento de la posición actual
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión con Selection Sort
ordenada = selection_sort(notas)
print(ordenada)  # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]  # copia para no romper el original
copia.sort()
print(copia)  # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)  # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)  # ['a', 'el', 'python', 'código']