class Temperaturas():

    def __init__(self):
        self.unidad = "Celsius"

    def celsiusAFahrenheit(self, grados):
        return (grados * 9/5) + 32

    def fahrenheitACelsius(self, grados):
        return (grados - 32) * 5/9

    def esCaluroso(self, grados):
        if grados >= 30:
            return "Hace calor"
        else:
            return "Temperatura agradable"


temp = Temperaturas()

print(temp.celsiusAFahrenheit(25))
print(temp.fahrenheitACelsius(86))
print(temp.esCaluroso(35))