print("gestión de información")

# =========================
# LISTAS Y TUPLAS
# =========================

frutas = ["plátano", "manzana", "piña"]

print(frutas[0])
print(frutas[1])

frutas_tupla = ("plátano", "manzana", "piña")

print(frutas_tupla[0])
print(frutas_tupla[1])
21
# =========================
# DICCIONARIO ANIDADO
# =========================

persona = {
    "nombre": "Gustavo ",
    "apellidos": "Gomez",
    "correo": "Gustavogz0714@gmail.com",
    "edad": 21,
    "telefonos": [
        {
            "tipo": "fijo",
            "numero": 9677755
        },
        {
            "tipo": "movil",
            "numero": 623455746
        }
    ]
}

print("\nDatos de la persona:")
print(persona)

print("\nTeléfono móvil:")
print(persona["telefonos"][1]["numero"])

# =========================
# CONVERSIÓN DE TIPOS
# =========================

edad = input("\nDime tu edad: ")
entero = int(edad)
doble = entero * 2

print("El doble de tu edad es:", doble)

# =========================
# ARGUMENTOS POR CONSOLA
# =========================

import sys

print("\nArgumentos recibidos:")
print(sys.argv)

if len(sys.argv) > 1:

    edad = sys.argv[1]
    edad_int = int(edad)

    print("El doble de la edad es:", edad_int * 2)

if len(sys.argv) > 2:

    nombre = sys.argv[1]
    edad = sys.argv[2]

    edad_int = int(edad)

    print("Hola", nombre, "tienes", edad_int * 2, "años (doble calculado)")