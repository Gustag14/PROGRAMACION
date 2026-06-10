class Cliente():

    def __init__(self, nombre, apellidos, email, direccion):

        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion


clientes = []

print("Gestor de clientes")

while True:

    print("\n1. Añadir cliente")
    print("2. Ver clientes")
    print("3. Eliminar último cliente")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")
        direccion = input("Introduce la dirección: ")

        nuevoCliente = Cliente(nombre, apellidos, email, direccion)

        clientes.append(nuevoCliente)

        print("Cliente añadido correctamente")

    elif opcion == "2":

        if len(clientes) == 0:
            print("No hay clientes registrados")

        else:

            for cliente in clientes:

                print("\nNombre:", cliente.nombre)
                print("Apellidos:", cliente.apellidos)
                print("Email:", cliente.email)
                print("Dirección:", cliente.direccion)

    elif opcion == "3":

        if len(clientes) > 0:

            clientes.pop()

            print("Último cliente eliminado")

        else:

            print("No hay clientes para eliminar")

    elif opcion == "4":

        print("Programa finalizado")
        break

    else:

        print("Opción incorrecta")