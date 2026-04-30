import threading
import time

# Fncion target del hilo
def tarea_con_error():
    time.sleep(2)
    resultado = 10 / 0 # Linea que genera el erro de indeterminación
    print(resultado)

# Crea el hilo
hilo = threading.Thread(target=tarea_con_error)

# Comienza el hilo
hilo.start()

# Tarea hilo principal
for i in range(5):
    print(f"Programa principal: {i}")
    time.sleep(1)

# Espera fin del hilo
hilo.join()

print("Fin")