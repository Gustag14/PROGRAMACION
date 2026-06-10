class Personaje:
    def __init__(self):
        self.nombre = ""
        self.nivel = 1

    def atacar(self):
        print(self.nombre, "realiza un ataque")

jugador1 = Personaje()
jugador1.nombre = "Guerrero"
jugador1.nivel = 5

jugador2 = Personaje()
jugador2.nombre = "Mago"
jugador2.nivel = 7

print("Personaje:", jugador1.nombre)
print("Nivel:", jugador1.nivel)
jugador1.atacar()

print("Personaje:", jugador2.nombre)
print("Nivel:", jugador2.nivel)
jugador2.atacar()