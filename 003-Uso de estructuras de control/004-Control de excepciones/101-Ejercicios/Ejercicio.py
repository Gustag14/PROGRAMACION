try:
    entradas = int(input("Introduce el número de entradas vendidas: "))
    capacidad = int(input("Introduce la capacidad del local: "))

    porcentaje = (entradas / capacidad) * 100

    print("Ocupación del local:", round(porcentaje, 2), "%")

except ZeroDivisionError:
    print("Error: la capacidad no puede ser 0.")

except ValueError:
    print("Error: debes introducir números válidos.")

finally:
    print("Fin del programa.")