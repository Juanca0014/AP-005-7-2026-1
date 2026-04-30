import threading
import time
import random
import queue

cola_cruda = queue.Queue()
cola_procesada = queue.Queue()
detener = threading.Event()

# En este programa el flujo de datos(Pipe) esta segmentado por operaciones lo que se llama pipeline

# Funcion target hilo 1
def leer_sensor():
    # Se ejecuta mientras el evento detener no este en set()
    while not detener.is_set():
        valor = random.uniform(0, 5)  # Simula lectura del sensor
        cola_cruda.put(valor)         # Envia datos por la primera cola
        print(f"Sensor: {valor:.2f}")
        time.sleep(0.5)

# Funcion target 2
def procesar_datos():
    # Se ejecuta mientras el evento detenern no este en set() y la priemra cola no este vacia
    while not detener.is_set() or not cola_cruda.empty():
        try: # Intenta procesar el dato de la cola
            valor = cola_cruda.get(timeout=0.2) # Recive el dato de la primera cola
            valor_procesado = valor * 2
            cola_procesada.put(valor_procesado) # Reenvia el dato de la segunda cola
            cola_cruda.task_done()              # Avisa que la primera cola esta libre
        except queue.Empty: # Si falla y la cola estaba vacia ignora
            pass

# Funcion target 3
def guardar_datos():
    # Ejecuta con archivo .txt abierto
    with open("datos_procesados.txt", "w", encoding="utf-8") as archivo:
        # Se ejecuta si el evento detener no es set o si la segunda cola no esta vacia
        while not detener.is_set() or not cola_procesada.empty():
            try: # intenta imprimir y guardar los datos
                valor = cola_procesada.get(timeout=0.2) # Obtine los datos de la segunda cola
                archivo.write(f"{valor:.2f}\n")         # Escribe en el .txt
                print(f"Guardado: {valor:.2f}")         # Imprime en el serial
                cola_procesada.task_done()              # Avisa que la segunda cola esta libre
            except queue.Empty:
                pass

# Crea hilos          
hilo_sensor = threading.Thread(target=leer_sensor)
hilo_procesamiento = threading.Thread(target=procesar_datos)
hilo_guardado = threading.Thread(target=guardar_datos)

# Inicia hilos
hilo_sensor.start()
hilo_procesamiento.start()
hilo_guardado.start()

# Tarea hilo principal
time.sleep(20)
# Evento
detener.set()

# Espera final de los hilos
hilo_sensor.join()
hilo_procesamiento.join()
hilo_guardado.join()

print("Programa terminado")