class Personaje:
    """Clase que representa un personaje simple."""
    
    def __init__(self, nombre, salud, fuerza):
        self.nombre = nombre
        self.salud = salud
        self.fuerza = fuerza
    
    def atacar(self, objetivo):
        """Ataca a otro personaje"""
        print(self.nombre + " ataca a " + objetivo.nombre)
        objetivo.recibir_ataque(self.fuerza)
    
    def recibir_ataque(self, dano):
        """Recibe daño y reduce la salud"""
        self.salud = self.salud - dano
        if self.salud < 0:
            self.salud = 0
        print(self.nombre + " recibe " + str(dano) + " de daño. Salud actual: " + str(self.salud))


# --- Programa principal ---
print("BATALLA ENTRE PERSONAJES\n")

# Crear dos personajes
p1 = Personaje("Gusta", 100, 20)
p2 = Personaje("Dani", 90, 15)

# Simular pelea
p1.atacar(p2)
p2.atacar(p1)

print("\n--- Estado Final ---")
print(p1.nombre + ": " + str(p1.salud) + " de salud")
print(p2.nombre + ": " + str(p2.salud) + " de salud")