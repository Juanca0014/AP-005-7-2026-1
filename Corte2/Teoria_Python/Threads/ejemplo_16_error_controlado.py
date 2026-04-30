import threading
import time

# Funcion target hilo
def tarea_con_error_controlado():
    try: # Intenta realizar la division
        time.sleep(2)
        resultado = 10 / 0
        print(resultado)
    except ZeroDivisionError:   # Cuando falla salta a la excepcion pero no aborta el programa
        print("Error dentro del thread: division por cero")

# Crea hilo
hilo = threading.Thread(target=tarea_con_error_controlado)

# Comienza hilo
hilo.start()

# Tarea del hilo principal
for i in range(5):
    print(f"Programa principal: {i}")
    time.sleep(1)

# Espera el final del hilo si hace falta
hilo.join()

print("Fin")