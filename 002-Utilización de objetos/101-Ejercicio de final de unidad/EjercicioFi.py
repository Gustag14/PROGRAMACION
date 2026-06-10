import math
import datetime

# Entrada de datos con validación
asistentes = 0
while asistentes <= 0:
    asistentes = int(input("Introduce el número de asistentes: "))

asientosporfila = 0
while asientosporfila <= 0:
    asientosporfila = int(input("Introduce los asientos por fila: "))

# Fecha y hora actual
evento = datetime.datetime.now()

# Cálculos
filas = math.ceil(asistentes / asientosporfila)

mediasatisfaccion = (7.8 + 6.5 + 9.2) / 3
satisfaccion_redondeada = round(mediasatisfaccion)

codigo_sesion = round(math.pi * 100)

# Salida
print("\n--- INFORME DEL EVENTO ---")
print("Asistentes:", asistentes)
print("Asientos por fila:", asientosporfila)
print("Filas necesarias:", filas)

print("\nFecha y hora")
print("Año:", evento.year)
print("Mes:", evento.month)
print("Día:", evento.day)
print("Hora:", evento.hour)
print("Minuto:", evento.minute)
print("Segundo:", evento.second)

print("\nOtro dato")
print("Satisfacción media:", satisfaccion_redondeada)
print("Código de sesión:", codigo_sesion)