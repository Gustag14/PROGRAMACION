import sqlite3

# Crear o conectar a la base de datos
conexion = sqlite3.connect("videojuegos2026.db")

cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS juegos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    genero TEXT,
    plataforma TEXT
)
""")

# Insertar datos
cursor.execute("""
INSERT INTO juegos
(titulo, genero, plataforma)
VALUES
('Minecraft', 'Sandbox', 'PC')
""")

cursor.execute("""
INSERT INTO juegos
(titulo, genero, plataforma)
VALUES
('FIFA 26', 'Deportes', 'PlayStation')
""")

conexion.commit()

# Leer datos
cursor.execute("SELECT * FROM juegos")

for juego in cursor.fetchall():
    print(juego)

conexion.close()