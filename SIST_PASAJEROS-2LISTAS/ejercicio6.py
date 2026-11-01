#NUMEROS UNICOS
#Dada una lista con posibles duplicados, retornar una lista sin duplicados manteniendo el orden.

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de números con elementos duplicados.

# Proceso — qué hago con eso
# Filtrar los duplicados ya sea de forma manual comprobando existencia, 
# convirtiendo a un conjunto (set) o usando un diccionario (dict.fromkeys).

# Salida — qué debo mostrar
# Una lista limpia únicamente con los elementos únicos.


#2 "BOSQUEJO A MANO:"
# nums = [1, 3, 2, 3, 4, 1, 5, 2]
# unicos = []

# x = 1 → no está → unicos = [1]
# x = 3 → no está → unicos = [1, 3]
# x = 2 → no está → unicos = [1, 3, 2]
# x = 3 → ya está → se omite
# x = 4 → no está → unicos = [1, 3, 2, 4]
# x = 1 → ya está → se omite
# x = 5 → no está → unicos = [1, 3, 2, 4, 5]
# x = 2 → ya está → se omite

# Resultado final: [1, 3, 2, 4, 5]


#3 "DESCUBRIR EL PATRON:"
# Filtrar manualmente preserva el orden iterando y validando duplicados. 
# Usar `set()` es muy rápido pero desordena los elementos. 
# `dict.fromkeys()` es la solución ideal en Python para eliminar duplicados de forma rápida y manteniendo el orden original.


#4 "ESCRIBIR EL CODIGO:"
nums = [1, 3, 2, 3, 4, 1, 5, 2]

# Manual (mantiene orden)
unicos = []
for x in nums:
    if x not in unicos:
        unicos.append(x)
print(unicos)                       # [1, 3, 2, 4, 5]

# Rápido (NO mantiene orden)
print(list(set(nums)))

# Rápido MANTENIENDO orden (Python 3.7+)
print(list(dict.fromkeys(nums)))    # [1, 3, 2, 4, 5]