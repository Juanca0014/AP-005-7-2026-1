import threading
import time

# Funcion target de los hilos
def simular_sensor(nombre_sensor, unidad, minimo, maximo):
    for i in range(5):
        valor = (minimo + maximo) / 2
        print(f"{nombre_sensor}: {valor} {unidad}")
        time.sleep(1)

# Crear hilos
sensor_temperatura = threading.Thread(
    target=simular_sensor,
    args=("Sensor de temperatura", "C", 20, 30)
)

sensor_distancia = threading.Thread(
    target=simular_sensor,
    args=("Sensor de distancia", "cm", 5, 50)
)

# Comenzar hilos
sensor_temperatura.start()
sensor_distancia.start()

# espera del hilo principal hasta que terminen los otros dos hilos
sensor_temperatura.join()
sensor_distancia.join()

# Regresa al hilo principal
print("Lecturas simuladas terminadas")