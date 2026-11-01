#INVERTIR UNA LISTA
#Invertir el orden de una lista sin usar lista.reverse().

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de elementos.

# Proceso — qué hago con eso
# Invertir el orden de sus elementos recorriendo índices hacia atrás o usando funciones nativas.

# Salida — qué debo mostrar
# Una nueva lista con los elementos en orden inverso.


#2 "BOSQUEJO A MANO:"
# lista = [1, 2, 3, 4, 5]
# Bucle con range(4, -1, -1) (índices: 4, 3, 2, 1, 0)
# i = 4 → 5
# i = 3 → 4
# i = 2 → 3
# i = 1 → 2
# i = 0 → 1
# Resultado: [5, 4, 3, 2, 1]


#3 "DESCUBRIR EL PATRON:"
# Recorrer la lista de atrás hacia adelante muestra cómo funcionan los índices inversos,
# pero Python lo resuelve de forma directa con slicing ([::-1]) o con la función `reversed()`.


#4 "ESCRIBIR EL CODIGO:""
lista = [1, 2, 3, 4, 5]

# Con bucle
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Con slicing (pythonic)
print(lista[::-1])

# Con reversed
print(list(reversed(lista)))