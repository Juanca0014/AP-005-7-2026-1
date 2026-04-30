import threading
import time
import random

# Función target
def leer_sensor():
    while True:
        # simula lectura del sensor cada 1 segundo
        valor = random.uniform(20.0, 30.0)
        print(f"Temperatura simulada: {valor:.2f} C")
        time.sleep(1)

# Crea hilo
hilo_sensor = threading.Thread(target=leer_sensor, daemon=True)
# Inicia hilo
hilo_sensor.start()

# Programa en primer plano
for i in range(10):
    print(f"Programa principal sigue activo: {i}")
    time.sleep(0.5)

print("Programa terminado")