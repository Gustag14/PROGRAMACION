class Cliente():

    def __init__(self, nombre, apellidos, email, direccion):

        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion

    def setEmail(self, nuevoEmail):

        self.email = nuevoEmail

    def getEmail(self):

        return self.email


cliente1 = Cliente("Juan", "Garcia", "juan@gmail.com", "Calle Mayor 12")
cliente2 = Cliente("Maria", "Lopez", "maria@gmail.com", "Avenida del Sol 8")
cliente3 = Cliente("Pedro", "Martinez", "pedro@gmail.com", "Calle Valencia 25")


print("Email original de Juan:", cliente1.getEmail())
cliente1.setEmail("juan.garcia@gmail.com")
print("Nuevo email de Juan:", cliente1.getEmail())

print()

print("Email original de Maria:", cliente2.getEmail())
cliente2.setEmail("maria.lopez@gmail.com")
print("Nuevo email de Maria:", cliente2.getEmail())

print()

print("Email original de Pedro:", cliente3.getEmail())
cliente3.setEmail("pedro.martinez@gmail.com")
print("Nuevo email de Pedro:", cliente3.getEmail())