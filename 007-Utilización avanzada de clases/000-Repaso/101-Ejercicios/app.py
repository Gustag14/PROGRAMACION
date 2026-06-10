import random
import json
import math
from flask import Flask, render_template

app = Flask(__name__)

# ======================
# CLASE ROBOT
# ======================

class Robot:

    def __init__(self, x, y, tamaño, direccion, velocidad):
        self.x = x
        self.y = y
        self.tamaño = tamaño
        self.direccion = direccion
        self.velocidad = velocidad

    def mover(self):
        # Movimiento aleatorio
        self.direccion += (random.random() - 0.5) * 0.3

        self.x += math.cos(self.direccion) * self.velocidad
        self.y += math.sin(self.direccion) * self.velocidad

        # Rebote paredes
        if self.x < 0 or self.x > 550:
            self.direccion += math.pi

        if self.y < 0 or self.y > 550:
            self.direccion += math.pi
            
    def diccionario(self):
        return {
            "x": self.x,
            "y": self.y,
            "tamano": self.tamaño
        }
# ======================
# CREAR ROBOTS
# ======================

robots = []

for i in range(40):
    robots.append(
        Robot(
            random.randint(0, 550),
            random.randint(0, 550),
            random.randint(15, 35),
            random.random() * math.pi * 2,
            random.random() * 4
        )
    )

# ======================
# RUTA HTML
# ======================

@app.route("/")
def inicio():
    return render_template("juego.html")

# ======================
# API
# ======================

@app.route("/api")
def api():
    for robot in robots:
        robot.mover()

    datos = []
    for robot in robots:
        datos.append(robot.diccionario())

    return json.dumps(datos)

# ======================
# INICIAR
# ======================

if __name__ == "__main__":
    app.run(debug=True)