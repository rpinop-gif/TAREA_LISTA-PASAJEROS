import os


def borrar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


def leer_entero(mensaje):
    """Solicita un número entero y valida la entrada."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def menu(titulo, opciones):
    """Muestra un menú y devuelve la opción seleccionada."""
    print(f"\n========== {titulo} ==========")

    for opcion in opciones:
        print(f" {opcion}")

    lon = len(opciones) - 1

    return input(f"Opción[0...{lon}]: ").strip().upper()

if __name__== "__main__":
    opc= menu ("Menú Principal", ["1) Pila", "2) Cola", "0) Salir"])
    opc1= menu ("Menú Pila", ["1) entrar a la pilar", "2) listar", "3) desapilar", "4) Cargar datos de prueba"])
    opc2= menu ("Menú Cola", ["1) entrar a la Cola", "2) listar", "3) desencolar", "4) Cargar datos de prueba"])