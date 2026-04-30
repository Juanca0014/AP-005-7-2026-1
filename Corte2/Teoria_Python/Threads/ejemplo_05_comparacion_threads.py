import threading
import time

# Funcion target del hilo
def tarea(nombre):
    print(f"Iniciando {nombre}")
    time.sleep(2)
    print(f"Terminando {nombre}")

# Empieza  contar tiempo
inicio = time.perf_counter()

# Crea lista vacia
hilos = []

# crea n=3 hilos, los añade a la lista y los inicia
for i in range(3):
    hilo = threading.Thread(target=tarea, args=(f"Tarea {i + 1}",))
    hilos.append(hilo)
    hilo.start()

# se queda esperando al final de cada hilo
for hilo in hilos:
    hilo.join()

# Temina de contar tiempo
fin = time.perf_counter()

# Imprime el tiempo total 
# t=2s, 4s mas rapido que secuencial
# se demora lo de una sola tarea
print(f"Tiempo total: {fin - inicio:.2f} segundos")