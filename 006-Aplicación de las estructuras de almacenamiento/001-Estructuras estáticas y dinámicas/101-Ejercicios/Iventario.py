import json

print("Inventario de videojuegos v1.0")

lista_videojuegos = []

try:
    archivo = open("videojuegos.json", "r")
    lista_videojuegos = json.load(archivo)
    archivo.close()
except:
    pass

while True:

    print("\nSelecciona una opción")
    print("1.- Añadir videojuego")
    print("2.- Listar videojuegos")
    print("3.- Eliminar último videojuego")
    print("4.- Salir")

    opcion = int(input("Tu opción: "))

    if opcion == 1:

        nombre = input("Nombre del videojuego: ")
        plataforma = input("Plataforma: ")

        lista_videojuegos.append({
            "nombre": nombre,
            "plataforma": plataforma
        })

        archivo = open("videojuegos.json", "w")
        json.dump(lista_videojuegos, archivo)
        archivo.close()

        print("Videojuego añadido correctamente")

    elif opcion == 2:

        print("Lista de videojuegos:")

        for juego in lista_videojuegos:
            print("Nombre:", juego["nombre"])
            print("Plataforma:", juego["plataforma"])
            print("---------------------")

    elif opcion == 3:

        if len(lista_videojuegos) > 0:

            lista_videojuegos.pop()

            archivo = open("videojuegos.json", "w")
            json.dump(lista_videojuegos, archivo)
            archivo.close()

            print("Videojuego eliminado")

        else:

            print("No hay videojuegos para eliminar")

    elif opcion == 4:

        print("Hasta pronto")
        break

    else:

        print("Opción incorrecta")