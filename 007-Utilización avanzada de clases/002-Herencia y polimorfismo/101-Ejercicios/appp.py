class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def dameDatos(self):
        return self.marca + " " + self.modelo


class Coche(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def dameDatos(self):
        return "Coche: " + self.marca + " " + self.modelo


class Moto(Vehiculo):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def dameDatos(self):
        return "Moto: " + self.marca + " " + self.modelo


coche1 = Coche("Toyota", "fortuner")
print(coche1.dameDatos())

moto1 = Moto("Bmw", "ga1200")
print(moto1.dameDatos())