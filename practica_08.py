limites_fabrica = (0,110)
print("Limite máximo de la cama", limites_fabrica[1])

temperatura_actual = 20
temperatura_objetivo = 60


print("Iniciando precalentamiento...")

while temperatura_actual < temperatura_objetivo:

    print("Temperatura actual: {}°C".format(temperatura_actual))


    temperatura_actual = temperatura_actual + 10

print("¡Temperatura objetivo alcanzada! Imprimiendo...")    