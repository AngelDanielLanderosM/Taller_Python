cliente_actual = {
    'nombre': 'Taller del Ajolote',
    'piezas_solicitadas': 15,
    'material': 'PETG'
}

cliente_actual['piezas_solicitadas'] = 20


print("Cliente:", cliente_actual['nombre'])
print("Piezas solicitadas:", cliente_actual['piezas_solicitadas'])



codigo_pieza = "soporte_motor_v2"
codigo_limpio = codigo_pieza.upper()
print("Código grabado:", codigo_limpio)




diagnostico_auto = {
    'modelo': 'Ford Fiesta',
    'falla_motor': False,
    'falla_electrica': True
}

if 'falla_electrica' in diagnostico_auto and diagnostico_auto['falla_electrica'] == True:
        print("Revisar cableado del coche")
else:
        print("Sistema eléctrico estable")