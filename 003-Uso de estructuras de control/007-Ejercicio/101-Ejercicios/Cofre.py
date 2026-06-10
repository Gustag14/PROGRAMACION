def poderBase(edad):
    """
    Devuelve el poder base del pirata según su experiencia.
    """
    if edad < 30:
        return 5
    elif edad < 100:
        return 8
    else:
        return 10


# Entrada de datos
edad_pirata = input("Introduce la edad del pirata: ")

try:
    edad_pirata = int(edad_pirata)
except:
    edad_pirata = 100

# Clasificación
if edad_pirata < 30:
    rango = "Novato"
elif edad_pirata < 100:
    rango = "Capitán"
else:
    rango = "Leyenda"

# Poder
poder = poderBase(edad_pirata)

# Cofre protegido
energia_cofre = 15

for turno in range(1, 3):

    if turno == 1:
        ataque = "Sable"
        dano = poder // 2
    else:
        ataque = "Cañón"
        dano = poder // 3

    assert isinstance(dano, (int, float))
    assert dano >= 0

    energia_cofre -= dano

    if energia_cofre < 0:
        energia_cofre = 0

    assert energia_cofre >= 0

    print("Turno", turno)
    print("Ataque:", ataque)
    print("Daño:", dano)
    print("Energía del cofre:", energia_cofre)

    if energia_cofre == 0:
        break

# Resultado final
print("\n--- RESUMEN ---")
print("Edad:", edad_pirata)
print("Rango:", rango)
print("Poder base:", poder)
print("Energía final del cofre:", energia_cofre)

if energia_cofre == 0:
    print("¡El pirata abre el cofre!")
else:
    print("El cofre sigue protegido.")