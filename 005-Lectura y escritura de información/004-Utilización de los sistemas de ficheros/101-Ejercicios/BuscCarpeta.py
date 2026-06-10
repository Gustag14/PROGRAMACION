import os

carpeta = input("Introduce una carpeta: ")

archivo_mapa = open("informe_archivos.txt", "w")

total = 0

for directorio, carpetas, archivos in os.walk(carpeta):

    for archivo in archivos:

        ruta = os.path.join(directorio, archivo)

        try:
            tamaño = os.path.getsize(ruta)
            total += tamaño

            archivo_mapa.write(ruta + " - " + str(tamaño) + " bytes\n")

        except:
            pass


archivo_mapa.close()

print("INFORME GENERADO")

print("Tamaño total de la carpeta:", total / (1024 * 1024), "MB")


# BUSCADOR
buscar = input("\nIntroduce texto a buscar en rutas: ")

archivo = open("informe_archivos.txt", "r")

lineas = archivo.readlines()

print("\nRESULTADOS:\n")

for linea in lineas:
    if buscar in linea:
        print(linea.strip())

archivo.close()