#CONTAR APARICIONES DE UN VALOR
#Dada una lista de números y un valor, contar cuántas veces aparece.

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de números y un valor a buscar (v)

# Proceso — qué hago con eso
# Recorrer la lista elemento por elemento comparando si cada número es igual a v, 
# o usar el método nativo de Python para contar ocurrencias.

# Salida — qué debo mostrar
# El número total de veces que aparece el valor en la lista.


#2 "BOSQUEJO A MANO:"
# lista = [1, 3, 2, 3, 4, 3, 5], v = 3
# count = 0

# x = 1 → 1 == 3 (Falso)  → count = 0
# x = 3 → 3 == 3 (Verdadero) → count = 1
# x = 2 → 2 == 3 (Falso)  → count = 1
# x = 3 → 3 == 3 (Verdadero) → count = 2
# x = 4 → 4 == 3 (Falso)  → count = 2
# x = 3 → 3 == 3 (Verdadero) → count = 3
# x = 5 → 5 == 3 (Falso)  → count = 3

# Resultado final: 3 aparece 3 veces.


#3 "DESCUBRIR EL PATRON:"
# El conteo manual recorre linealmente la estructura acumulando coincidencias en una variable de control.
# Python encapsula esta lógica repetitiva de manera ultra eficiente en el método incorporado `lista.count(v)`, 
# el cual está escrito y optimizado en C por debajo.


#4 "ESCRIBIR EL CODIGO:"
lista = [1, 3, 2, 3, 4, 3, 5]
v = 3

# Manual
count = 0
for x in lista:
    if x == v:
        count += 1
print(f"{v} aparece {count} veces")

# Pythonic
print(f"{v} aparece {lista.count(v)} veces")