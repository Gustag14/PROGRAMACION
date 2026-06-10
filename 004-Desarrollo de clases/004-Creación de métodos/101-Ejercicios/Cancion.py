class Cancion():
    # Constructor
    def __init__(self):
        self.__titulo = ""
        self.__artista = ""

    # Setters
    def setTitulo(self, nuevoTitulo):
        self.__titulo = nuevoTitulo

    def setArtista(self, nuevoArtista):
        self.__artista = nuevoArtista

    # Getters
    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista


# Lista vacía para almacenar canciones
canciones = []

print("🎵Gestor de canciones")

while True:
    print("\nSelecciona una opción:")
    print("1.- Añadir canción")
    print("2.- Ver canciones")
    print("3.- Salir")

    try:
        opcion = int(input("Escoge una opción: "))
    except:
        print("Debes introducir un número.")
        continue

    if opcion == 1:
        print("\nAñadir nueva canción")

        nuevaCancion = Cancion()

        titulo = input("Título: ")
        artista = input("Artista: ")

        nuevaCancion.setTitulo(titulo)
        nuevaCancion.setArtista(artista)

        canciones.append(nuevaCancion)

        print(" Canción añadida correctamente")

    elif opcion == 2:
        print("\nListado de canciones")

        if len(canciones) == 0:
            print("No hay canciones registradas")
        else:
            for cancion in canciones:
                print("----------------------")
                print("Título:", cancion.getTitulo())
                print("Artista:", cancion.getArtista())

    elif opcion == 3:
        print("Hasta pronto ")
        break

    else:
        print("Opción incorrecta")