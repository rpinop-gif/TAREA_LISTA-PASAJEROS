from pasajero import Pasajero


class MiLista:
    """Lista construida a mano sobre un arreglo de tamaño fijo."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # Insertar un pasajero en una posición
    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            return False
        if posicion < 0 or posicion > self.cantidad:
            return False

        for i in range(self.cantidad, posicion, -1):
            self.datos[i] = self.datos[i - 1]

        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    # Buscar un pasajero por su número
    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return self.datos[i]
        return None

    # Buscar un pasajero mediante búsqueda binaria
    def buscar_binaria(self, numero):
        inicio = 0
        fin = self.cantidad - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if self.datos[medio].numero == numero:
                return self.datos[medio]
            elif self.datos[medio].numero < numero:
                inicio = medio + 1
            else:
                fin = medio - 1

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
        if posicion < 0 or posicion >= self.cantidad:
            return None

        eliminado = self.datos[posicion]

        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None

        return eliminado

    # Eliminar un pasajero según su número
    def eliminar_por_valor(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                self.eliminar_por_posicion(i)
                return True

        return False

    # Ordenar pasajeros de menor a mayor número
    def ordenar_asc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    # Ordenar pasajeros de mayor a menor número
    def ordenar_desc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    # Invertir el orden de los pasajeros
    def reversar(self):
        inicio = 0
        fin = self.cantidad - 1

        while inicio < fin:
            aux = self.datos[inicio]
            self.datos[inicio] = self.datos[fin]
            self.datos[fin] = aux

            inicio = inicio + 1
            fin = fin - 1

    # Crear una copia de la lista
    def copiar(self):
        nueva_lista = MiLista(self.capacidad)

        for i in range(self.cantidad):
            nueva_lista.datos[i] = self.datos[i]

        nueva_lista.cantidad = self.cantidad
        return nueva_lista

    # Obtener la cantidad de pasajeros
    def longitud(self):
        return self.cantidad