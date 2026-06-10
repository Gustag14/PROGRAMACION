import pickle

class Producto():

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio


# Creamos lista de productos
productos = []

productos.append(Producto("Teclado", 25))
productos.append(Producto("Raton", 15))
productos.append(Producto("Monitor", 120))


# Guardar en archivo binario
archivo = open("productos.bin", "wb")
pickle.dump(productos, archivo)
archivo.close()


# Leer archivo binario
archivo = open("productos.bin", "rb")
datos = pickle.load(archivo)
archivo.close()


print("LISTA DE PRODUCTOS:\n")

for producto in datos:
    print(producto.nombre, "-", producto.precio, "€")


# Trabajo con archivo de texto
archivo = open("registro.txt", "w")
archivo.write("Producto añadido correctamente\n")
archivo.write("Sistema iniciado\n")
archivo.close()


archivo = open("registro.txt", "r")
lineas = archivo.readlines()

print("\nREGISTRO:\n")

for linea in lineas:
    print(linea.strip())