def monitorear_temperatura(grados):
    if grados > 50:
        return "Alerta: Riesgo de deformación"
    else:
        return "Secado en estado optimo"

resultado = monitorear_temperatura(60)
print("Prueba 1:", resultado)


def validar_material(tipo_plastico):
    if "PETG" in tipo_plastico or "ABS" in tipo_plastico:
        return "Aprobado Resistente a temperatura de cabina"
    elif "PLA" in tipo_plastico:
        return "Rechazado: Se va a derretir"
    else:
        return "Material no especificado"

resultado_material = validar_material("PLA")
print("Prueba 2:", resultado_material)





def revisar_malla(es_solido_cerrado, tiene_interferencias):
    if es_solido_cerrado == True and tiene_interferencias == False:
        return "Malla limpia, lista para exportar a CAD"
    else:
        return "Malla defectuosa, requiere post-procesamiento"

resultado_malla = revisar_malla(True, False)
print("Prueba 3:", resultado_malla)
