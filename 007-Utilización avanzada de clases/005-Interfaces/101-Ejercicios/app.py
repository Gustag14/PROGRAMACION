from PIL import Image

imagen = Image.open(r"C:\Users\Gustavo Gomez\Downloads\Programacion\meme.png")

imagen = imagen.convert("RGB")

anchura, altura = imagen.size

for x in range(anchura):
    for y in range(altura):
        rojo, verde, azul = imagen.getpixel((x, y))

        imagen.putpixel((x, y), (
            255 - rojo,
            255 - verde,
            255 - azul
        ))

imagen.save("meme_modificado.png")

print("Imagen modificada correctamente")

print("Imagen modificada correctamente")