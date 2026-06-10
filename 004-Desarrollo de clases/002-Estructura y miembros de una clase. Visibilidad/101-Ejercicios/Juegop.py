class Videojuego:
    def __init__(self):
        self.nombre = ""
        self.genero = ""

juegos = []

while True:

    print("\nGESTOR DE VIDEOJUEGOS")
    print("1. Añadir videojuego")
    print("2. Ver videojuegos")
    print("3. Eliminar último videojuego")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nuevo = Videojuego()
        nuevo.nombre = input("Nombre del juego: ")
        nuevo.genero = input("Género: ")
        juegos.append(nuevo)

    elif opcion == "2":
        if len(juegos) == 0:
            print("No hay videojuegos registrados")
        else:
            for juego in juegos:
                print("Nombre:", juego.nombre)
                print("Género:", juego.genero)
                print("-----------")

    elif opcion == "3":
        if len(juegos) > 0:
            juegos.pop()
            print("Videojuego eliminado")
        else:
            print("No hay videojuegos para eliminar")

    elif opcion == "4":
        break

    else:
        print("Opción no válida")