#CRUD DE PASAJEROS CON CLASE PASAJERO+LIST
#Sistema completo: agregar, listar, buscar por cédula, modificar y eliminar pasajeros. Usa clase Pasajero y una list como contenedor.

#1 "ENTENDER EL PROBLEMA:"
#--Entrada — qué me dan
# opción del menú y datos

#Proceso — qué hago con eso
#operaciones sobre la lista con validaciones

#Salida — qué debo mostrar
#resultado de cada acción

#2 "BOSQUEJO A MANO:"
#class Pasajero(nombre, cedula)

# lista = []
# menú:
#   1. Agregar    → lista.append(Pasajero(...))
#   2. Listar     → for p in lista: print(p)
#   3. Buscar     → next((p for p in lista if p.cedula==ced), None)
#   4. Modificar  → buscar + p.nombre = nuevo
#   5. Eliminar   → lista[:] = [p for p in lista if p.cedula != ced]
#   6. Salir      → break

#3 "DESCUBRIR EL PATRÓN:"
#El truco elegante para buscar es next((p for p in lista if p.cedula == ced), None):
# recorre la lista hasta encontrar el primero que cumple, o retorna None si no existe.

#Para eliminar hay dos formas: (a) lista.remove(p) con el objeto encontrado, o (b) reconstruir la lista sin él con list comprehension.
#  La segunda es más «pythonica».

#4 "ESCRIBIR EL CÓDIGO:"
class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)


# --- Programa principal ---
lista = []

while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        break

    # Ahora tú
#Añade una opción «Ordenar por nombre» que use lista.sort(key=lambda p: p.nombre).

class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)


# --- Programa principal ---
lista = []

while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Ordenar por nombre 7.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        if not lista:
            print("No hay pasajeros para ordenar")
        else:
            lista.sort(key=lambda p: p.nombre)
            print("Lista ordenada por nombre ✓")

    elif op == "7":
        break