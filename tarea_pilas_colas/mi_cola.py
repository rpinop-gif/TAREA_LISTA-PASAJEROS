from pasajero import Pasajero


class MiCola:
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La cola está llena")
            return False

        if self.buscar(pasajero.numero) != -1:
            print("  El número de pasajero ya existe")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (cola vacía)")
            return

        for i in range(self.cantidad):
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desencolar(self):
        if self.cantidad == 0:
            print("  La cola está vacía")
            return None

        pasajero = self.datos[0]

        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1

        return pasajero

    def ver_frente(self):
        if self.cantidad == 0:
            print("  La cola está vacía")
            return None

        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i

        return -1


    def ordenar(self):
            if self.cantidad <= 1:
                return True
    
            for i in range(self.cantidad - 1):
                for j in range(self.cantidad - 1 - i):
                    if self.datos[j].numero > self.datos[j + 1].numero:
                        aux = self.datos[j]
                        self.datos[j] = self.datos[j + 1]
                        self.datos[j + 1] = aux

    def buscar_binaria(self, numero):
        izquierda = 0
        derecha = self.cantidad - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2

            if self.datos[medio].numero == numero:
                return medio
            elif self.datos[medio].numero < numero:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return -1


        return True

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            return False

        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento

        return True

    def eliminar_por_numero(self, numero):
        if self.cantidad == 0:
            print("  La cola está vacía")
            return None

        eliminado = None
        cantidad_original = self.cantidad

        for i in range(cantidad_original):
            pasajero = self.desencolar()

            if pasajero.numero == numero:
                eliminado = pasajero
            else:
                self.encolar(pasajero)

        return eliminado

    def copiar(self):
        nueva_cola = MiCola(self.capacidad)

        for i in range(self.cantidad):
            nueva_cola.encolar(self.datos[i])

        return nueva_cola

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0