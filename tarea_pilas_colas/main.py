from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from utils import borrar_pantalla, leer_entero, menu


# Crear las estructuras
pila = MiPila(10)
cola = MiCola(10)


# ---------------- FUNCIONES DE APOYO ----------------

def leer_pasajero():
    """Solicita los datos necesarios para registrar un pasajero."""

    numero = leer_entero("Número de pasajero: ")
    nombre = input("Nombre: ").strip()
    cedula = input("Cédula: ").strip()
    edad = leer_entero("Edad: ")
    fecha = input("Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("Destino: ").strip()
    asiento = input("Asiento: ").strip().upper()

    return Pasajero(
        numero, nombre, cedula, edad,
        fecha, destino, asiento
    )


def datos_prueba():
    """Retorna cinco pasajeros de prueba en orden de llegada."""

    return [
        Pasajero(1005, "Diana", "0923456789", 22,
                 "2026-11-15", "Quito", "12A"),

        Pasajero(1002, "Ana", "0912345678", 28,
                 "2026-11-15", "Lima", "03C"),

        Pasajero(1009, "Luis", "0987654321", 35,
                 "2026-11-20", "Bogotá", "18F"),

        Pasajero(1004, "Beto", "0934567890", 16,
                 "2026-11-20", "Quito", "07B"),

        Pasajero(1001, "Elena", "0901234567", 41,
                 "2026-11-22", "Lima", "01A")
    ]


# ---------------- MENÚ DE LA PILA ----------------

def menu_pila():

    while True:
        borrar_pantalla()

        opciones = [
            "1) Apilar pasajero",
            "2) Listar pasajeros",
            "3) Desapilar pasajero",
            "4) Ver tope",
            "5) Buscar pasajero",
            "6) Modificar pasajero",
            "7) Eliminar por número",
            "8) Copiar pila",
            "9) Longitud / ¿Está vacía?",
            "C) Cargar datos de prueba",
            "0) Volver al menú principal"
        ]

        op = menu("MENÚ PILA (LIFO)", opciones)

        if op == "1":
            pasajero = leer_pasajero()

            if pila.apilar(pasajero):
                print("Pasajero agregado a la pila.")

        elif op == "2":
            pila.listar()

        elif op == "3":
            pasajero = pila.desapilar()

            if pasajero is not None:
                print("Pasajero desapilado:")
                print(pasajero)

        elif op == "4":
            pasajero = pila.ver_tope()

            if pasajero is not None:
                print("Pasajero que está en el tope:")
                print(pasajero)

        elif op == "5":
            numero = leer_entero("Ingrese el número del pasajero: ")
            posicion = pila.buscar(numero)

            if posicion != -1:
                print("Pasajero encontrado:")
                print(pila.datos[posicion])
            else:
                print("Pasajero no encontrado.")

        elif op == "6":
            numero = leer_entero("Número del pasajero a modificar: ")
            destino = input("Nuevo destino: ").strip()
            asiento = input("Nuevo asiento: ").strip().upper()

            if pila.modificar(numero, destino, asiento):
                print("Pasajero modificado correctamente.")
            else:
                print("Pasajero no encontrado.")

        elif op == "7":
            numero = leer_entero("Número del pasajero a eliminar: ")
            pasajero = pila.eliminar_por_numero(numero)

            if pasajero is not None:
                print("Pasajero eliminado:")
                print(pasajero)
            else:
                print("Pasajero no encontrado.")

        elif op == "8":
            copia = pila.copiar()
            print("Copia de la pila:")
            copia.listar()

        elif op == "9":
            print("Cantidad de pasajeros:", pila.longitud())
            print("¿La pila está vacía?:", pila.esta_vacia())

        elif op == "C":
            for pasajero in datos_prueba():
                pila.apilar(pasajero)

            print("Datos de prueba cargados en la pila.")

        elif op == "0":
            break

        else:
            print("Opción no válida.")

        input("\nPresione Enter para continuar...")


# ---------------- MENÚ DE LA COLA ----------------

def menu_cola():

    while True:
        borrar_pantalla()

        opciones = [
            "1) Encolar pasajero",
            "2) Listar pasajeros",
            "3) Desencolar pasajero",
            "4) Ver frente",
            "5) Buscar pasajero",
            "6) Modificar pasajero",
            "7) Eliminar por número",
            "8) Copiar cola",
            "9) Longitud / ¿Está vacía?",
            "C) Cargar datos de prueba",
            "0) Volver al menú principal"
        ]

        op = menu("MENÚ COLA (FIFO)", opciones)

        if op == "1":
            pasajero = leer_pasajero()

            if cola.encolar(pasajero):
                print("Pasajero agregado a la cola.")

        elif op == "2":
            cola.listar()

        elif op == "3":
            pasajero = cola.desencolar()

            if pasajero is not None:
                print("Pasajero desencolado:")
                print(pasajero)

        elif op == "4":
            pasajero = cola.ver_frente()

            if pasajero is not None:
                print("Pasajero que está al frente:")
                print(pasajero)

        elif op == "5":
            numero = leer_entero("Ingrese el número del pasajero: ")
            posicion = cola.buscar(numero)

            if posicion != -1:
                print("Pasajero encontrado:")
                print(cola.datos[posicion])
            else:
                print("Pasajero no encontrado.")

        elif op == "6":
            numero = leer_entero("Número del pasajero a modificar: ")
            destino = input("Nuevo destino: ").strip()
            asiento = input("Nuevo asiento: ").strip().upper()

            if cola.modificar(numero, destino, asiento):
                print("Pasajero modificado correctamente.")
            else:
                print("Pasajero no encontrado.")

        elif op == "7":
            numero = leer_entero("Número del pasajero a eliminar: ")
            pasajero = cola.eliminar_por_numero(numero)

            if pasajero is not None:
                print("Pasajero eliminado:")
                print(pasajero)
            else:
                print("Pasajero no encontrado.")

        elif op == "8":
            copia = cola.copiar()
            print("Copia de la cola:")
            copia.listar()

        elif op == "9":
            print("Cantidad de pasajeros:", cola.longitud())
            print("¿La cola está vacía?:", cola.esta_vacia())

        elif op == "C":
            for pasajero in datos_prueba():
                cola.encolar(pasajero)

            print("Datos de prueba cargados en la cola.")

        elif op == "0":
            break

        else:
            print("Opción no válida.")

        input("\nPresione Enter para continuar...")


# ---------------- MENÚ PRINCIPAL ----------------

def main():

    while True:
        borrar_pantalla()

        opciones = [
            "1) Pila",
            "2) Cola",
            "0) Salir"
        ]

        op = menu("MENÚ PRINCIPAL", opciones)

        if op == "1":
            menu_pila()

        elif op == "2":
            menu_cola()

        elif op == "0":
            print("¡Programa finalizado!")
            break

        else:
            print("Opción no válida.")
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()