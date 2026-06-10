stock = 15

try:
    assert stock > 0, "No quedan productos disponibles"
    print("Producto disponible")
except AssertionError as e:
    print("Error:", e)