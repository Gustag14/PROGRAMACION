import json

# Guardamos artículos en un JSON (simulación de base de datos)
articulos = [
    {
        "titulo": "Receta de pasta",
        "fecha": "2026-01-08",
        "autor": "Ana garciaa",
        "contenido": "Aprende a cocinar una deliciosa pasta con tomate."
    },
    {
        "titulo": "Viaje a la montaña",
        "fecha": "2026-01-02",
        "autor": "Señor carlitos alberto",
        "contenido": "Experiencia de senderismo en los Pirineos."
    }
]

# Guardar en archivo JSON
archivo = open("contenido.json", "w")
json.dump(articulos, archivo)
archivo.close()


# Leer JSON
archivo = open("contenido.json", "r")
datos = json.load(archivo)
archivo.close()

print("LISTA DE ARTÍCULOS\n")

for articulo in datos:
    print("###########")
    print(articulo["titulo"])
    print(articulo["fecha"])
    print(articulo["autor"])
    print(articulo["contenido"])
    print("###########\n")


# Simulación de lectura de TXT
archivo = open("comentarios.txt", "w")
archivo.write("Buen articulo\nMuy interesante\nMe gusto mucho\n")
archivo.close()

archivo = open("comentarios.txt", "r")
comentarios = archivo.readlines()

print("COMENTARIOS:\n")

for c in comentarios:
    print(c.strip())