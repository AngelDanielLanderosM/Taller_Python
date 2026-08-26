def calcular_desperdicio(longitud_barra, longitud_pieza):
    piezas_enteras = longitud_barra // longitud_pieza
    merma = longitud_barra % longitud_pieza
    return piezas_enteras, merma

# Prueva de maquinado
piezas, sobrante = calcular_desperdicio(100, 30)

print("Podemos maquinar {} piezas enteras.".format(piezas))
print("Nos quedara un sobrante de {} mm de material.".format(sobrante))