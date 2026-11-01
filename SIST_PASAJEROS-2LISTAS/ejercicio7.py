#SEGUNDO MAYOR
#Encontrar el segundo número más grande de una lista (sin ordenar toda la lista).

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de números desordenada.

# Proceso — qué hago con eso
# Recorrer la lista una sola vez manteniendo dos variables de control (el mayor y el segundo mayor), 
# actualizándolas conforme encontramos números más grandes.

# Salida — qué debo mostrar
# El número mayor y el segundo mayor valor de la lista.


#2 "BOSQUEJO A MANO:"
# nums = [5, 2, 9, 7, 9, 3, 8]
# Inicial: mayor = -inf, segundo = -inf

# n = 5 → 5 > mayor (-inf) → segundo = -inf, mayor = 5
# n = 2 → 2 > 5 (no), 2 > -inf y 2 < 5 → segundo = 2 (mayor = 5)
# n = 9 → 9 > 5 (sí) → segundo = 5, mayor = 9
# n = 7 → 7 > 9 (no), 7 > 5 y 7 < 9 → segundo = 7 (mayor = 9)
# n = 9 → 9 > 9 (no), 9 > 7 y 9 < 9 (falso) → sin cambios
# n = 3 → 3 > 9 (no), 3 > 7 (falso) → sin cambios
# n = 8 → 8 > 9 (no), 8 > 7 y 8 < 9 → segundo = 8 (mayor = 9)

# Resultado final: Mayor: 9, Segundo: 8.


#3 "DESCUBRIR EL PATRON:"
# Rastrear los dos valores más altos en una sola pasada ($O(n)$) evita ordenar la lista completa, 
# actualizando de forma inteligente al campeón actual y desplazando al anterior al puesto de segundo.


#4 "ESCRIBIR EL CODIGO:"
nums = [5, 2, 9, 7, 9, 3, 8]

# Dos campeones: mayor y segundo
mayor = float("-inf")
segundo = float("-inf")

for n in nums:
    if n > mayor:
        segundo = mayor         # el que era mayor pasa a segundo
        mayor = n
    elif n > segundo and n < mayor:
        segundo = n

print(f"Mayor: {mayor}")
print(f"Segundo: {segundo}")