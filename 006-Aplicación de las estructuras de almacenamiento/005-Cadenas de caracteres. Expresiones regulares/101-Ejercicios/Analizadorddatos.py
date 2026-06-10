import re
import requests

print("Datos de usuarios ")

nombre = "Gustavoo"

print(nombre)
print(nombre[0])

for letra in nombre:
    print(letra)

print(len(nombre))

print(nombre.split(" "))

datos = "gutavogz0714@gmail.com"
print(datos)

partido = datos.split(",")
print(partido)

archivo = open("clientes.csv", "r")

lineas = archivo.readlines()

clientes = []

for linea in lineas:
    limpio = linea.replace("\n", "")
    cliente = limpio.split(",")
    clientes.append(cliente)

archivo.close()

print(clientes)

cadena = "Hoy es lunes"
print(cadena.replace("lunes", "martes"))

patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email = "info@empresa.com"

print(re.match(patron_email, email))

patron_direccion = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+ [0-9]{5}$'

direccion = "Calle 28n41-68"

print(re.match(patron_direccion, direccion))

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:3b-instruct",
    "prompt": "Explica qué es una lista en Python con ejemplo sencillo en español.",
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()

print(data["response"])