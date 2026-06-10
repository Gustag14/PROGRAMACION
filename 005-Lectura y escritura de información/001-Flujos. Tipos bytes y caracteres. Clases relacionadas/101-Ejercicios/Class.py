while True:

    print("\nGestor de tareas")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:

        tarea = input("Introduce una tarea: ")

        archivo = open("tareas.txt", "a")

        archivo.write(tarea + "\n")

        archivo.close()

        print("Tarea guardada correctamente")

    elif opcion == 2:

        archivo = open("tareas.txt", "r")

        lineas = archivo.readlines()

        if len(lineas) == 0:
            print("No hay tareas registradas")

        else:
            print("\nLista de tareas:")

            for linea in lineas:
                print(linea.strip())

        archivo.close()

    elif opcion == 3:

        print("Programa finalizado")
        break

    else:

        print("Opción incorrecta")