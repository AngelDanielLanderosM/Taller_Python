import time



temperatura_actual = 20
temperatura_objetivo = 60


print("Iniciando precalentamiento (Velocidad real)...")

while temperatura_actual < temperatura_objetivo:
    print("Temperatura actual: {}°C".format(temperatura_actual))
    temperatura_actual = temperatura_actual + 10

    time.sleep(1)

print("¡Temperatura objetivo alcanzada! Imprimiendo...")    