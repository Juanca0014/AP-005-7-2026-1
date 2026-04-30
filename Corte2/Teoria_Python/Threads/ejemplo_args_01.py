import threading
import time

def saludar(nombre):  # Funcion target del hilo
    for i in range(3):
        print(f"Hola, {nombre}. Mensaje {i}")
        time.sleep(1)

hilo = threading.Thread(target=saludar, args=("Ana",)) # Creación del hilo
hilo.start()                                           # Iniciar el hilo
hilo.join()                                            # Se queda en espera para ejecutar hasta
                                                       # que el hilo donde se llama (principal)
print("Fin del programa")