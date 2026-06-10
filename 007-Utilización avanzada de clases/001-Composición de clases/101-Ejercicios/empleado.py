class Empleado:
    def __init__(self, nombre, apellidos, email, departamento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.departamento = departamento

    def dameDatos(self):
        return self.nombre + " " + self.apellidos


class Desarrollador(Empleado):
    def __init__(self, nombre, apellidos, email, departamento):
        super().__init__(nombre, apellidos, email, departamento)


class Diseñador(Empleado):
    def __init__(self, nombre, apellidos, email, departamento):
        super().__init__(nombre, apellidos, email, departamento)


class DesarrolladorFrontend(Desarrollador):
    def __init__(self, nombre, apellidos, email, departamento):
        super().__init__(nombre, apellidos, email, departamento)


class DesarrolladorBackend(Desarrollador):
    def __init__(self, nombre, apellidos, email, departamento):
        super().__init__(nombre, apellidos, email, departamento)


empleado1 = Empleado("Laura", "Martínez", "laura@empresa.com", "General")
print(empleado1.dameDatos())

desarrollador1 = Desarrollador("Carlos", "Gómez", "carlos@empresa.com", "Informática")
print(desarrollador1.dameDatos())

frontend1 = DesarrolladorFrontend("Ana", "López", "ana@empresa.com", "Frontend")
print(frontend1.dameDatos())

backend1 = DesarrolladorBackend("Miguel", "Sánchez", "miguel@empresa.com", "Backend")
print(backend1.dameDatos())