import math

Cuadros = int(input("Introduce el número de cuadros: "))
Pinturas = int(input("Introduce el número de Pinturas: "))

cuadros = math.ceil(Pinturas / Cuadros)

print("Necesitas", cuadros, "cuadros")