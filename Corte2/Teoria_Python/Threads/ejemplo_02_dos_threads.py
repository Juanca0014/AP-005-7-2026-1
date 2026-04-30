import threading
import time


def contar(nombre): # Funcion target de los hilos
    for i in range(5):
        print(f"{nombre}: {i}")
        time.sleep(1)

# envia argumento al hilo con args=(arg)
hilo_a = threading.Thread(target=contar, args=("Hilo A",))  # Crea un hilo secundario
hilo_b = threading.Thread(target=contar, args=("Hilo B",))  # Crea un segundo hilo secundario

# Iniciar los hilos con el metodo start()
hilo_a.start()
hilo_b.start()