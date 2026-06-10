print("Calculadora de IVA")

base_imponible = float(input("Introduce la base imponible: "))

iva = base_imponible * 0.21
total = base_imponible + iva

print("IVA:", iva)
print("Total:", total)