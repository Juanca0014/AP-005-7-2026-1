import threading
import time
detener = threading.Event()

# Funcion target del hilo
def tarea_periodica(nombre, periodo):
    # Se ejecuta hasta que el evento sea set
    while not detener.is_set():
        # Comienza a contar tiempo
        # Prgunta tiempo de inicio
        inicio = time.perf_counter()
        
        print(f"{nombre}: ejecutando tarea")
        
        # Pregunta tiempo actual y calcula tiempo de ejecucion
        tiempo_usado = time.perf_counter() - inicio
        # Obtiene le tiempo que resta del periodo tras la ejecucion
        tiempo_restante = periodo - tiempo_usado
        # Espera el tiempo para completar el periodo
        if tiempo_restante > 0:
            time.sleep(tiempo_restante)

# Crea hilo
hilo = threading.Thread(target=tarea_periodica, args=("Monitor", 1.0))
# Inicia el hilo
hilo.start()

# Tarea del hilo principal
time.sleep(6)

# Evento que detiene los hilos
detener.set()
# Espera el final de los hilos
hilo.join()

print("Fin")