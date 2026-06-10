"""
Control de plazas para una excursión
"""

aforo_total = int(input("Número de plazas disponibles: "))
precio = float(input("Precio por plaza: "))

aforo_restante = aforo_total
plazas_reservadas = 0
recaudacion = 0
ventas = 0

while True:

    try:
        cantidad = int(input("¿Cuántas plazas quieres reservar?: "))

        if cantidad <= 0:
            print("Cantidad no válida")
            continue

        if cantidad > aforo_restante:
            print("Solo quedan", aforo_restante, "plazas")
            respuesta = input("¿Reservar las plazas restantes? (S/N): ")

            if respuesta.upper() == "S":
                cantidad = aforo_restante
            else:
                continue

        plazas_reservadas += cantidad
        aforo_restante -= cantidad
        recaudacion += cantidad * precio
        ventas += 1

        assert aforo_restante >= 0
        assert plazas_reservadas + aforo_restante == aforo_total

        print("Reserva realizada")

        if ventas % 5 == 0:
            print("⏱ Descanso técnico")

        if aforo_restante == 0:
            print("Excursión completa")
            break

    except ValueError:
        print("Debes introducir un número")
        continue

print("\n--- RESUMEN ---")
print("Plazas reservadas:", plazas_reservadas)
print("Recaudación:", recaudacion, "€")

if aforo_restante == 0:
    print("Estado: Completo")
else:
    print("Quedan", aforo_restante, "plazas libres")