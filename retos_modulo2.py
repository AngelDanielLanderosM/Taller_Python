def calcular_soportes(bobina, consumo_pieza):
    soportes_completos = bobina // consumo_pieza
    sobrante = bobina % consumo_pieza
    return soportes_completos, sobrante

# Producción de Soportes Automotrices
soportes, sobrante = calcular_soportes(1000, 250)

print("Podemos imprimir {} soportes completos.".format(soportes))
print("Nos quedara un sobrante de {} gramos de filamento".format(sobrante))




def calcular_lote(largo_cama, largo_pieza):
    piezas_en_una_sola_fila = largo_cama // largo_pieza
    espacio_sobrante_orilla_cama = largo_cama % largo_pieza
    return piezas_en_una_sola_fila, espacio_sobrante_orilla_cama

# Optimización de la Cama de Impresión
piezas, espacio_sobrante = calcular_lote(256, 54)

print("Podemos imprimir {} piezas en una sola fila.".format(piezas))
print("Nos quedara un sobrante de {} mm de espacio en la orilla de la cama.".format(espacio_sobrante))





def convertir_tiempo(minutos_totales):
    horas = minutos_totales // 60
    minutos = minutos_totales % 60
    return horas, minutos

# Temporizador del Laminador
horas, minutos = convertir_tiempo(125)

print("El tiempo total de laminado es de {} horas y {} minutos.".format(horas, minutos))


