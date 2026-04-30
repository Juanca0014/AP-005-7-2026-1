import time

# Funcion de tareas
def tarea(nombre):
    print(f"Iniciando {nombre}")
    time.sleep(2)
    print(f"Terminando {nombre}")

inicio = time.perf_counter() # Empieza a medir tiempo

tarea("Tarea 1") # ejecuta primero tarea 1
tarea("Tarea 2") # cuando termina tarea 1 ejecuta tarea 2
tarea("Tarea 3") # cuando termina tarea 2 ejecuta tarea 3

fin = time.perf_counter() # Termina de medir tiempo

# Imprime el tiempo total
# t=6s 2s por cada una de las tareas
print(f"Tiempo total: {fin - inicio:.2f} segundos")