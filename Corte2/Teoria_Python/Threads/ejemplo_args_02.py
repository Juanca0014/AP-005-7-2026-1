import threading
import time

# Funcion target de los hilos
def contar(nombre, inicio, fin, pausa):
    for numero in range(inicio, fin + 1):
        print(f"{nombre}: {numero}")
        time.sleep(pausa)

# Crea los hilos con argumentos
hilo_1 = threading.Thread(
    target=contar,
    args=("Contador rapido", 1, 5, 0.5)  # equivale a contar("Contador rapido", 1, 5, 0.5)
)
hilo_2 = threading.Thread(
    target=contar,
    args=("Contador lento", 10, 15, 1.0) # equivale a contar("Contador rapido", 1, 5, 1.0)
)

# Inicia los hilos
hilo_1.start()
hilo_2.start()

# Esperas en el hilo principal hasta que se terminen de ejecutar los hilos secundarios
hilo_1.join()
hilo_2.join()