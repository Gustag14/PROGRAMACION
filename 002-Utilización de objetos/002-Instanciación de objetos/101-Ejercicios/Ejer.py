# Importamos las herramientas básicas necesarias
from datetime import datetime
import random

# 1. Fecha de inicio del juego
fecha = datetime.now()

# 2. Puntuación inicial aleatoria entre 0 y 10
puntuacion = random.random() * 10
puntuacion = round(puntuacion, 2)   # Redondeamos a 2 decimales

# 3. Mostrar resultados
print("Bienvenido al juego, Gusta ")
print("Fecha de inicio del juego:", fecha)
print("Tu puntuación inicial es:", puntuacion)