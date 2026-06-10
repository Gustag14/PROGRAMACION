def calcularDescuento(precio, descuento):
    """
    Calcula el precio final aplicando un descuento.
    Devuelve 0 si los datos no son válidos.
    """

    try:
        precio = float(precio)
        descuento = float(descuento)

        if precio < 0 or descuento < 0:
            return 0

        return precio - (precio * descuento / 100)

    except:
        return 0


print(calcularDescuento(100, 20))
print(calcularDescuento("50", "10"))