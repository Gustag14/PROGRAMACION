totallibro = 0

for anio in range(2020, 2026):
    for mes in range(1, 13):
        for dia in range(1, 31):
            print("Día", dia, "del mes", mes, "del año", anio, ": 10 préstamos realizados")
            totallibro += 10

print("Total de préstamos realizados:", totallibro)