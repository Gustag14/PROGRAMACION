class Cancion:
    def __init__(self):
        self.titulo = ""
        self.artista = ""
        self.generos = []


canciones = []

print("Gestor de música")

while True:

    print("\n1. Añadir canción")
    print("2. Ver canciones")
    print("3. Eliminar última canción")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        nuevaCancion = Cancion()

        nuevaCancion.titulo = input("Título de la canción: ")
        nuevaCancion.artista = input("Artista: ")

        genero1 = input("Primer género musical: ")
        genero2 = input("Segundo género musical: ")

        nuevaCancion.generos.append(genero1)
        nuevaCancion.generos.append(genero2)

        canciones.append(nuevaCancion)

        print("Canción añadida correctamente")

    elif opcion == "2":

        if len(canciones) == 0:
            print("No hay canciones registradas")

        else:
            for cancion in canciones:
                print("\nTítulo:", cancion.titulo)
                print("Artista:", cancion.artista)
                print("Géneros:", cancion.generos)

    elif opcion == "3":

        if len(canciones) > 0:
            canciones.pop()
            print("Canción eliminada")
        else:
            print("No hay canciones para eliminar")

    elif opcion == "4":
        break

    else:
        print("Opción no válida")