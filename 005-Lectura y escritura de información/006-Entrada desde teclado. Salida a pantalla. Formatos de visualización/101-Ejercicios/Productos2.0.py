import pickle

class Producto():

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio


print("###### GESTIÓN DE PRODUCTOS v1.0 ######")

productos = []

# Cargar datos si existen
try:
    archivo = open("productos.bin", "rb")
    productos = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo previo, se crea uno nuevo")


while True:

    # Guardar siempre al inicio del bucle
    archivo = open("productos.bin", "wb")
    pickle.dump(productos, archivo)
    archivo.close()

    print("\n1. Insertar producto")
    print("2. Listar productos")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Escoge una opción: ")

    if opcion == "1":

        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))

        productos.append(Producto(nombre, precio))

        print("Producto añadido")

    elif opcion == "2":

        if len(productos) == 0:
            print("No hay productos")

        else:
            identificador = 0
            for producto in productos:
                print("ID:", identificador)
                print("Nombre:", producto.nombre)
                print("Precio:", producto.precio)
                print("----------------")
                identificador += 1

    elif opcion == "3":

        identificador = int(input("ID del producto a modificar: "))

        nombre = input("Nuevo nombre: ")
        precio = float(input("Nuevo precio: "))

        productos[identificador].nombre = nombre
        productos[identificador].precio = precio

        print("Producto actualizado")

    elif opcion == "4":

        identificador = int(input("ID del producto a eliminar: "))
        confirmacion = input("¿Seguro? (s/n): ").lower()

        if confirmacion == "s":
            productos.pop(identificador)
            print("Producto eliminado")
        else:
            print("Cancelado")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción incorrecta")