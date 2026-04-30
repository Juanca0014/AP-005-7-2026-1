import threading
import time
detener = threading.Event() # Crea el evento de hilo

# Funcion target
def tarea_periodica():
    # Ejecutar solo si evento set no ha ocurrido
    while not detener.is_set():
        print("Tarea trabajando...")
        time.sleep(1)
    
    # Se ejecuta cuando set ocurrio
    print("La tarea recibio la orden de detenerse")

# Crea hilo
hilo = threading.Thread(target=tarea_periodica)

# Comenzar hilo
hilo.start()

# Ejecución del hilo principal
time.sleep(5)

# evento en detener con metodo set()
print("Solicitando detener el thread")
detener.set()

# Espera fin del hilo
hilo.join()

print("Programa terminado correctamente")
