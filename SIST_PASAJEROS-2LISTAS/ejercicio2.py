#ESTADISTICA DE UNA LISTA DE NOTAS
#Dada una lista de N notas, calcular:
#  promedio, máxima, mínima, cantidad de aprobados y el nombre del mejor estudiante (paralelo con nombres).


#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# N, lista de nombres y lista de notas

# Proceso — qué hago con eso
# recorridos en paralelo para calcular estadísticas

# Salida — qué debo mostrar
# todas las métricas

#2 "BSOQUEJO A MANO:"
# nombres = ["Ana", "Luis", "Diana"]
# notas   = [ 8,     6,      10 ]

# promedio = (8+6+10) / 3 = 8.0
# máxima   = 10 (índice 2 → Diana)
# aprobados = 2 (8>=7, 10>=7)

#3 "DESCUBRIR EL PATRON:"
# Este ejercicio junta 4 patrones en uno: acumulador (suma), campeón (máximo), contador (aprobados) y búsqueda (nombre del máximo).

# Fíjate en el uso de listas paralelas: nombres[i] y notas[i] se refieren a la misma persona. 
# En el módulo siguiente verás cómo un dict o una clase mejora esto.

#4 "ESCRIBIR EL CODIGO:"
nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas   = [ 8,     6,      10,      7,      5]

# Python trae todo esto:
print(f"Promedio: {sum(notas) / len(notas):.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

print(f"\nManual → prom: {suma/len(notas):.2f}, máx: {maxima}, aprob: {aprob_manual}")



# Ahora tú
# Añade la desviación estándar. Fórmula: sqrt(sum((n - prom)² for n in notas) / len(notas)).
import math

nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas = [8, 6, 10, 7, 5]

# --- Versión Python (con funciones integradas y math) ---
prom = sum(notas) / len(notas)
desviacion = math.sqrt(sum((n - prom) ** 2 for n in notas) / len(notas))

print(f"Promedio: {prom:.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")
print(f"Desviación estándar: {desviacion:.2f}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")


# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

prom_manual = suma / len(notas)

# Cálculo manual de la desviación estándar usando la fórmula
suma_cuadrados = 0
for n in notas:
    suma_cuadrados += (n - prom_manual) ** 2

desv_manual = (suma_cuadrados / len(notas)) ** 0.5

print(
    f"\nManual → prom: {prom_manual:.2f}, máx: {maxima}, "
    f"aprob: {aprob_manual}, desv: {desv_manual:.2f}"
)