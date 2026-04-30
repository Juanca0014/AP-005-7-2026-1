import threading
import time

# Funcion target del hilo
def tarea(nombre, duracion):
    print(f"Inicia {nombre}")
    time.sleep(duracion)
    print(f"Termina {nombre}")

# Crea el hilo
hilo_1 = threading.Thread(target=tarea, args=("Tarea 1", 3))
hilo_2 = threading.Thread(target=tarea, args=("Tarea 2", 2))

# Comienza el hilo
hilo_1.start()
hilo_2.start()

# Espera hasta que termine la ejecicion del hilo
hilo_1.join()
hilo_2.join()

# Fin del hilo principal
print("Todas las tareas terminaron")
