import os
import zipfile
import shutil

print("GESTOR DE COPIAS DE SEGURIDAD")

ruta = input("Introduce la carpeta a analizar: ").strip()

if not os.path.isdir(ruta):
    print("La ruta no es válida")

else:

    # Crear carpeta de backups
    backup = os.path.join(ruta, "backups")
    if not os.path.exists(backup):
        os.mkdir(backup)

    elementos = os.listdir(ruta)

    for elemento in elementos:

        origen = os.path.join(ruta, elemento)

        # Evitamos la carpeta de backups
        if origen == backup:
            continue

        # Si es archivo
        if os.path.isfile(origen):

            destino = os.path.join(backup, elemento + ".zip")

            archivozip = zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED)
            archivozip.write(origen, arcname=elemento)
            archivozip.close()

            print("Archivo comprimido:", elemento)

            os.remove(origen)

        # Si es carpeta
        elif os.path.isdir(origen):

            destino = os.path.join(backup, elemento + ".zip")

            archivozip = zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED)

            for directorio, subcarpetas, archivos in os.walk(origen):

                for archivo in archivos:

                    rutaarchivo = os.path.join(directorio, archivo)
                    rutarelativa = os.path.relpath(rutaarchivo, origen)

                    archivozip.write(rutaarchivo, rutarelativa)

            archivozip.close()

            print("Carpeta comprimida:", elemento)

            shutil.rmtree(origen)

print("PROCESO FINALIZADO")