perfil_impresora = {
    'marca': 'Bambu Lab',
    'modelo': 'A1 Mini',
    'estado': 'Imprimiendo',
    'horas_uso': 350
}

perfil_impresora['estado'] = 'En espera'

perfil_impresora['boquilla_instalada'] = 0.4

print("Reporte de equipo:", perfil_impresora['modelo'])
print("Estado actual:", perfil_impresora['estado'])