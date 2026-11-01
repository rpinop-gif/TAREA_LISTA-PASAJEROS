from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # Insertar un pasajero en una posición
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            return False

        self.pasajeros.insert(posicion, pasajero)
        return True

    # Buscar un pasajero por su número
    def buscar(self, numero):
        for p in self.pasajeros:
            if p.numero == numero:
                return p
        return None

    # Buscar un pasajero mediante búsqueda binaria
    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]
        posicion = bisect_left(numeros, numero)

        if posicion < len(self.pasajeros) and numeros[posicion] == numero:
            return self.pasajeros[posicion]

        return None

    # Modificar destino y asiento de un pasajero
    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pasajero = self.buscar(numero)

        if pasajero is None:
            return False

        pasajero.destino = nuevo_destino
        pasajero.asiento = nuevo_asiento
        return True

    # Eliminar un pasajero según su posición
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None

        return self.pasajeros.pop(posicion)

    # Eliminar un pasajero según su número
    def eliminar_por_valor(self, numero):
        for i, p in enumerate(self.pasajeros):
            if p.numero == numero:
                self.pasajeros.pop(i)
                return True

        return False

    # Ordenar pasajeros de menor a mayor número
    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    # Ordenar pasajeros de mayor a menor número
    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    # Invertir el orden de los pasajeros
    def reversar(self):
        self.pasajeros.reverse()

    # Crear una copia de la lista
    def copiar(self):
        nueva_lista = ListaPython()
        nueva_lista.pasajeros = self.pasajeros.copy()
        return nueva_lista

    # Obtener la cantidad de pasajeros
    def longitud(self):
        return len(self.pasajeros)

    # Filtrar pasajeros según su destino
    def filtrar_por_destino(self, destino):
        return [p for p in self.pasajeros if p.destino.lower() == destino.lower()]

    # Obtener pasajeros mayores de edad
    def mayores_de_edad(self):
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]