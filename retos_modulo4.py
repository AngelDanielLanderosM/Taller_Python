refacciones_extrusor = ["Termistor", "Cartucho Calefactor", "Boquilla 0.4"]
refacciones_extrusor.append("ventilador 5015")
print(refacciones_extrusor)






tableros_pendientes = ["MDF 18mm", "Triplay 15mm", "Melamina Blanca"]
tableros_pendientes.append("Pino 20mm")
for material in tableros_pendientes:
    print("Enviado a sierra circular: {}".format(material))






medidas_lote = [8.0, 7.9, 8.2, 8.0]
for medida in medidas_lote:
    if medida == 8.0:
        print("Pieza Aprobada")
    else:
        print("Pieza Rechazada")
