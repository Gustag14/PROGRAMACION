import pickle

print("Gestor de menú del restaurante 🍽️")

menu = []

# Intentamos cargar datos si el archivo existe
try:
    archivo = open("menu.bin", "rb")
    menu = pickle.load(archivo)
    archivo.close()
except:
    pass

while True:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1.- Añadir plato al menú")
    print("2.- Ver menú completo")
    print("3.- Guardar menú")
    print("4.- Cargar menú")
    print("5.- Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:

        comida = input("Introduce el nombre del plato: ")
        menu.append(comida)
        print("Plato añadido 👍")

    elif opcion == 2:

        print("\nPlatos disponibles en el menú:")

        if len(menu) == 0:
            print("El menú está vacío todavía...")
        else:
            for elemento in menu:
                print("-", elemento)

    elif opcion == 3:

        archivo = open("menu.bin", "wb")
        pickle.dump(menu, archivo)
        archivo.close()

        print("Menú guardado correctamente 💾")

    elif opcion == 4:

        archivo = open("menu.bin", "rb")
        menu = pickle.load(archivo)
        archivo.close()

        print("Menú cargado correctamente 📂")

    elif opcion == 5:

        print("Saliendo del programa... 👋")
        break

    else:

        print("Opción no válida")