import tkinter as tk
from tkinter import ttk
import mysql.connector


conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="empresadam"
)
cursor = conexion.cursor()


ventana = tk.Tk()
ventana.title("Gestión de Libros")
ventana.geometry("700x500")


# --- FUNCIONES ---

def insertar_libro():

    titulo_val = titulo.get()
    autor_val = autor.get()

    if titulo_val == "" or autor_val == "":
        print("Rellena todos los campos")
        return

    cursor.execute("""
        INSERT INTO libros VALUES (NULL, %s, %s);
    """, (titulo_val, autor_val))

    conexion.commit()
    cargar_datos()

    titulo.delete(0, tk.END)
    autor.delete(0, tk.END)


def cargar_datos():

    cursor.execute("SELECT * FROM libros;")
    filas = cursor.fetchall()

    tabla.delete(*tabla.get_children())

    for fila in filas:
        tabla.insert("", "end", values=fila)


# --- INTERFAZ ---

tk.Label(ventana, text="Título del libro").pack(pady=5)
titulo = tk.Entry(ventana)
titulo.pack(pady=5)

tk.Label(ventana, text="Autor").pack(pady=5)
autor = tk.Entry(ventana)
autor.pack(pady=5)

tk.Button(ventana, text="Insertar libro", command=insertar_libro).pack(pady=10)


tabla = ttk.Treeview(ventana, columns=("id", "titulo", "autor"), show="headings")
tabla.heading("id", text="ID")
tabla.heading("titulo", text="Título")
tabla.heading("autor", text="Autor")

tabla.pack(pady=20)


cargar_datos()

ventana.mainloop()