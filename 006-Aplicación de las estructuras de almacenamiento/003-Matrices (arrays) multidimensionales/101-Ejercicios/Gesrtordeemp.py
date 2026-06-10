import pickle

print("Bienvenidos al gestor")

agenda = []

# Cargar datos si existen
try:
    archivo = open("alumnos.bin", "rb")
    agenda = pickle.load(archivo)
    archivo.close()
except:
    pass

while True:

    print("\n1.- Añadir alumno")
    print("2.- Ver alumnos")
    print("3.- Guardar datos")
    print("4.- Salir")

    opcion = int(input("Elige una opción: 1"))

    if opcion == 1:

        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        email = input("Email: ")
        telefono = input("Teléfono: ")

        # MATRIZ (array dentro de array)
        agenda.append([nombre, apellidos, email, telefono])

        print("Alumno añadido 👍")

    elif opcion == 2:

        print("\nLista de alumnos:")

        for alumno in agenda:
            print("-------------------")
            print("Nombre:", alumno[0])
            print("Apellidos:", alumno[1])
            print("Email:", alumno[2])
            print("Teléfono:", alumno[3])

    elif opcion == 3:

        archivo = open("alumnos.bin", "wb")
        pickle.dump(agenda, archivo)
        archivo.close()

        print("Datos guardados correctamente ")

    elif opcion == 4:

        print("Saliendo")
        break

    else:

        print("Opción incorrecta")