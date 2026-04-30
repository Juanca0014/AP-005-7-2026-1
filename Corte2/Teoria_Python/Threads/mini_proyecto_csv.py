import threading
import time
import random
import queue
import csv

detener = threading.Event()
cola = queue.Queue()


def adquirir_datos():
    while not detener.is_set():
        tiempo = time.time()
        valor = random.uniform(0, 100)
        cola.put((tiempo, valor))
        time.sleep(0.25)


def guardar_csv():
    
    # Abre el archivo .csv
    with open("registro.csv", "w", newline="", encoding="utf-8") as archivo:
        
        # Escribe los los titulos de cada columna
        escritor = csv.writer(archivo)
        escritor.writerow(["tiempo", "valor"])

        # Se ejecuta mientras no se active el evento detener y la cola no esta vacia
        while not detener.is_set() or not cola.empty():
            
            try: # Intenta escribir los valores de la cola en el csv
                tiempo, valor = cola.get(timeout=0.2)           # Lee valroes de la cola
                escritor.writerow([tiempo, valor])              # Escribe una nueva fila
                print(f"Guardado: {tiempo:.2f}, {valor:.2f}")   # Avisa cola libre
                cola.task_done()
            
            except queue.Empty:
                pass

# Crear hilo
hilo_adquisicion = threading.Thread(target=adquirir_datos)
hilo_guardado = threading.Thread(target=guardar_csv)

# Comenzar hilo
hilo_adquisicion.start()
hilo_guardado.start()

# Tarea del hilo principal
print("Registrando datos durante 10 segundos...")
time.sleep(10)
detener.set()

# Espera hilo
hilo_adquisicion.join()
hilo_guardado.join()

print("Archivo registro.csv generado")