import threading
import time
import random
import queue
cola_datos = queue.Queue() # Crea cola

# Funcion target hilo_1
def productor():
    for i in range(10):
        dato = random.randint(1, 100)
        cola_datos.put(dato) # Envia datos por la cola
        print(f"Productor genero: {dato}")
        time.sleep(0.5)

# Funcion target hilo_2
def consumidor():
    for i in range(10):
        dato = cola_datos.get() # recibe datos de la cola
        print(f"Consumidor recibio: {dato}")
        cola_datos.task_done() # Avisa que ya proceso la cola

# Crea hilos
hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

# Inicia hilos
hilo_productor.start()
hilo_consumidor.start()

# Espera final de los hilos
hilo_productor.join()
hilo_consumidor.join()

print("Proceso terminado")