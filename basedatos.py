import sqlite3

conn = sqlite3.connect('turnos.db')
c = conn.cursor()

# Crear tabla si no existe
c.execute('''
CREATE TABLE IF NOT EXISTS turnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("Base de datos creada")
