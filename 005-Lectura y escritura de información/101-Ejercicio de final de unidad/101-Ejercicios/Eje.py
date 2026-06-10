import pickle
import os

# ====================== CLASE CLIENTE ======================
class Cliente:
    """Mini-clase Cliente"""
    def __init__(self, nombre, apellido, dni, email, telefono=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telefono = telefono


# ====================== CARGA DE DATOS ======================
archivo = "clientes.pkl"
clientes = []

# Intentamos cargar los clientes guardados previamente
if os.path.exists(archivo):
    try:
        with open(archivo, "rb") as f:
            clientes = pickle.load(f)
        print(f"Se cargaron {len(clientes)} clientes existentes.\n")
    except Exception as e:
        print(" Error al cargar el archivo. Se iniciará con lista vacía.")
        clientes = []
else:
    print("No existe archivo de clientes aún. Se creará uno nuevo.\n")


# ====================== MENÚ ======================
def mostrar_menu():
    print("\n" + "="*40)
    print("  GESTIÓN DE CLIENTES")
    print("="*40)
    print("1. Crear nuevo cliente")
    print("2. Listar clientes")
    print("3. Salir")
    print("="*40)


def guardar_clientes():
    """Guarda la lista de clientes usando pickle"""
    try:
        with open(archivo, "wb") as f:
            pickle.dump(clientes, f)
        print("Clientes guardados correctamente.")
    except Exception as e:
        print(f" Error al guardar: {e}")


# ====================== PROGRAMA PRINCIPAL ======================
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == "1":
        # Crear cliente
        print("\n--- Nuevo Cliente ---")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        dni = input("DNI: ").strip()
        email = input("Email: ").strip()
        telefono = input("Teléfono (opcional): ").strip()

        nuevo_cliente = Cliente(nombre, apellido, dni, email, telefono or None)
        clientes.append(nuevo_cliente)

        guardar_clientes()   # Guardamos cada vez que se crea uno

        print(f"Cliente {nombre} {apellido} creado exitosamente!")

    elif opcion == "2":
        # Listar clientes
        print("\n--- Lista de Clientes ---")
        if not clientes:
            print("No hay clientes registrados aún.")
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"{i}. {cliente.nombre} {cliente.apellido} - DNI: {cliente.dni} - Email: {cliente.email}")
                if cliente.telefono:
                    print(f"   Teléfono: {cliente.telefono}")
                print("-" * 50)

    elif opcion == "3":
        print("\n ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")