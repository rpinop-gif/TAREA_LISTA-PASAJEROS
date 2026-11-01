#FUSIONAR DOS LISTAS ORDENADAS
#Dadas dos listas ordenadas, fusionarlas en una tercera también ordenada, sin usar sort()

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Dos listas ordenadas de números (a y b).

# Proceso — qué hago con eso
# Recorrer ambas listas simultáneamente usando dos punteros (i, j), 
# comparando los elementos actuales y añadiendo el menor a una lista de resultados, 
# para finalmente anexar los elementos restantes de la lista que no haya terminado.

# Salida — qué debo mostrar
# Una única lista fusionada que mantiene el orden ascendente.


#2 "BOSQUEJO A MANO:"
# a = [1, 3, 5, 7], b = [2, 4, 6, 8, 10]
# i = 0 (1), j = 0 (2), resultado = []

# i=0, j=0: 1 <= 2 → resultado = [1], i = 1
# i=1, j=0: 3 <= 2 (Falso) → resultado = [1, 2], j = 1
# i=1, j=1: 3 <= 4 → resultado = [1, 2, 3], i = 2
# i=2, j=1: 5 <= 4 (Falso) → resultado = [1, 2, 3, 4], j = 2
# i=2, j=2: 5 <= 6 → resultado = [1, 2, 3, 4, 5], i = 3
# i=3, j=2: 7 <= 6 (Falso) → resultado = [1, 2, 3, 4, 5, 6], j = 3
# i=3, j=3: 7 <= 8 → resultado = [1, 2, 3, 4, 5, 6, 7], i = 4 (Fin de 'a')
# Fin del while. Añadimos restos: resultado.extend(b[3:]) → añade [8, 10]

# Resultado final: [1, 2, 3, 4, 5, 6, 7, 8, 10]


#3 "DESCUBRIR EL PATRON:"
# Fusionar listas con dos punteros permite combinar secuencias ordenadas de forma muy eficiente ($O(n + m)$), 
# seleccionando siempre el valor menor y vaciando los elementos sobrantes al final.


#4 "ESCRIBIR EL CODIGO:"
a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

resultado = []
i = j = 0

# Recorremos las dos listas a la par
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        resultado.append(a[i])
        i += 1
    else:
        resultado.append(b[j])
        j += 1

# Añadimos lo que quede de la más larga
resultado.extend(a[i:])
resultado.extend(b[j:])

print(resultado)                    # [1, 2, 3, 4, 5, 6, 7, 8, 10]