def inspeccion_calidad(medida):
    if medida == 30.0:
        return "Aprobado: Medida exacta."
    elif medida >= 29.5 and medida <= 30.5:
        return "Aprobado: Dentro de tolerancia."
    else:
        return "Rechazado: Pieza fuera de especificación."

# Pasamos tres piezas distintas por el sensor
pieza_1 = inspeccion_calidad(30.0)
pieza_2 = inspeccion_calidad(30.4)
pieza_3 = inspeccion_calidad(28.0)

print("Reporte Pieza 1:", pieza_1)
print("Reporte Pieza 2:", pieza_2)
print("Reporte Pieza 3:", pieza_3)
