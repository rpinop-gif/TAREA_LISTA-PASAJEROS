
# ==============================================================
#  lista_pasajeros.py · Lista enlazada de pasajeros
# ==============================================================

from pasajero import Pasajero


class Nodo:
    """Un vagón del tren: lleva un pasajero (data) y el enganche al siguiente (next)."""

    def __init__(self, data):
        self.data = data
        self.next = None


class ListaPasajeros:
    """Lista enlazada simple con todas las reservas del vuelo."""

    def __init__(self):
        self.head = None
        self.cantidad = 0

    def ingresar(self, pasajero):
        nuevo = Nodo(pasajero)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo

        self.cantidad = self.cantidad + 1
        return True

    # 1. Verificar si la lista está vacía
    def esta_vacia(self):
        return self.head is None

    # 2. Obtener la cantidad de pasajeros
    def longitud(self):
        return self.cantidad

    # 3. Listar todos los pasajeros
    def listar(self):
        resultado = []
        actual = self.head

        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next

        return resultado

    # 4. Buscar por número de reserva
    def buscar(self, numero):
        actual = self.head

        while actual is not None:
            if actual.data.numero == numero:
                return actual.data
            actual = actual.next

        return None

    # 5. Buscar por asiento
    def buscar_por_asiento(self, asiento):
        actual = self.head

        while actual is not None:
            if actual.data.asiento == asiento:
                return actual.data
            actual = actual.next

        return None

    # 6. Buscar por cédula
    def buscar_por_cedula(self, cedula):
        actual = self.head

        while actual is not None:
            if actual.data.cedula == cedula:
                return actual.data
            actual = actual.next

        return None

    # 7. Modificar un pasajero
    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        pasajero = self.buscar(numero)

        if pasajero is None:
            return False

        pasajero.nombre = nuevo_nombre
        pasajero.edad = nueva_edad
        pasajero.asiento = nuevo_asiento

        return True

    # 8. Eliminar un pasajero
    def eliminar(self, numero):
        if self.head is None:
            return None

        if self.head.data.numero == numero:
            eliminado = self.head.data
            self.head = self.head.next
            self.cantidad = self.cantidad - 1
            return eliminado

        anterior = self.head
        actual = self.head.next

        while actual is not None:
            if actual.data.numero == numero:
                eliminado = actual.data
                anterior.next = actual.next
                self.cantidad = self.cantidad - 1
                return eliminado

            anterior = actual
            actual = actual.next

        return None

    # 9. Filtrar pasajeros por clase
    def filtrar_por_clase(self, clase):
        resultado = []
        actual = self.head

        while actual is not None:
            if actual.data.clase() == clase:
                resultado.append(actual.data)
            actual = actual.next

        return resultado
