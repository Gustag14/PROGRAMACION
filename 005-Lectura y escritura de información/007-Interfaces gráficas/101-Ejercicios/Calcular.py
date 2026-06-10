import tkinter as tk

def calcular_media():

    n1 = float(nota1.get())
    n2 = float(nota2.get())
    n3 = float(nota3.get())

    media = (n1 + n2 + n3) / 3

    resultado.config(text="Media: " + str(media))


ventana = tk.Tk()
ventana.title("Calculadora de notas")

tk.Label(ventana, text="Introduce 3 notas").pack(pady=10)

nota1 = tk.Entry()
nota1.pack(pady=5)

nota2 = tk.Entry()
nota2.pack(pady=5)

nota3 = tk.Entry()
nota3.pack(pady=5)

tk.Button(ventana, text="Calcular media", command=calcular_media).pack(pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(pady=10)

ventana.mainloop()