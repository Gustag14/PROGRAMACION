edad = int(input("Introduce tu edad: "))

if edad < 8:
    categoria = "Pre-mini"
elif edad <= 11:
    categoria = "Mini"
elif edad <= 15:
    categoria = "Infantil"
elif edad <= 17:
    categoria = "Cadete"
elif edad <= 20:
    categoria = "Junior"
else:
    categoria = "Senior"

print("Tu categoría es:", categoria)