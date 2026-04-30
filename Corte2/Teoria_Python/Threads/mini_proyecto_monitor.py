import threading
import time
import random
import queue

detener = threading.Event()
cola_temperaturas = queue.Queue()

# Funcion target hilo 1
def sensor_temperatura():
    while not detener.is_set():
        temperatura = random.uniform(18.0, 32.0) # Simula sensor
        cola_temperaturas.put(temperatura) # Envia a la cola
        time.sleep(0.5)

def procesador_temperatura():
    lecturas = []
    # Funciona mientras no se active el evento detener
    while not detener.is_set() or not cola_temperaturas.empty():
        try: # Intenta procesar los datos enviados
            temperatura = cola_temperaturas.get(timeout=0.2) # obtiene los datos de la cola
            lecturas.append(temperatura)                     # guarda los datos en la lista
            # Si hay mas de 5 lecturas hace promedio
            if len(lecturas) > 5:
                lecturas.pop(0)
                promedio = sum(lecturas) / len(lecturas)
                
                print(
                f"Temperatura: {temperatura:.2f} C | "
                f"Promedio movil: {promedio:.2f} C"
                )

            cola_temperaturas.task_done()   # Avisa de cola libre
            
        except queue.Empty: # Excepcion de cola vacia
            pass

# Crea hilos
hilo_sensor = threading.Thread(target=sensor_temperatura)
hilo_procesador = threading.Thread(target=procesador_temperatura)

# Inicia hilos
hilo_sensor.start()
hilo_procesador.start()

print("Monitor iniciado")
print("Escribe ’salir’ para terminar")

# Tarea del hilo principal
while True:
    comando = input("> ")
    # Condicion de parada
    if comando.lower() == "salir":
        detener.set()
        break
    print("Comando no reconocido")

# Espera final del hilo
hilo_sensor.join()
hilo_procesador.join()
print("Monitor terminado")