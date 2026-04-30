import threading
import time

def saludar(): # Función del hilo
    for i in range(5):
        print("Hola desde el thread secundario")
        time.sleep(1)

hilo = threading.Thread(target=saludar)     # Crea el hilo usando como tarea la funcion saludar
hilo.start()                                # inicia el hilo con el metodo start()
print("Hola desde el programa principal")