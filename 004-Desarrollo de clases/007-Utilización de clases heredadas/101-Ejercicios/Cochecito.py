class Vehiculo():

    def __init__(self):

        self.marca = ""
        self.modelo = ""
        self.velocidad = 0


class Coche(Vehiculo):

    def __init__(self):

        super().__init__()
        self.numeroPuertas = 4


class Moto(Vehiculo):

    def __init__(self):

        super().__init__()
        self.cilindrada = 125


coche1 = Coche()
coche1.marca = "Seat"
coche1.modelo = "Ibiza"

moto1 = Moto()
moto1.marca = "Yamaha"
moto1.modelo = "MT-07"

print(coche1.marca)
print(moto1.marca)