# Entrada de datos
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto (€): "))
stock = int(input("Ingrese la cantidad en stock: "))

# Cálculos
IVA = 0.21
precio_con_iva = precio * (1 + IVA)

# Determinar disponibilidad y estado del stock
disponible = stock > 0
stock_bajo = stock < 5

# Salida de resultados
print("\n" + "="*40)
print("       REGISTRO DE PRODUCTO")
print("="*40)
print(f"Producto:          {nombre}")
print(f"Precio sin IVA:    {precio:.2f} €")
print(f"Precio con IVA:    {precio_con_iva:.2f} €")
print(f"Stock actual:      {stock} unidades")

if disponible:
    print("Estado:            Disponible")
else:
    print("Estado:            No disponible")

if stock_bajo and disponible:
    print("¡ALERTA!:          Stock bajo (menos de 5 unidades)")
elif stock == 0:
    print("¡ALERTA!:          Producto agotado")

print("="*40)