import threading
import time

# Funcion target del hilo
def tarea(nombre, repeticiones, pausa):
    for i in range(repeticiones):
        print(f"{nombre}: repeticion {i}")
        time.sleep(pausa)

# Crear el hilo
hilo = threading.Thread(
    target=tarea,
    # kwargs permitee enviar los datos como diccionarios
    kwargs={
        "nombre": "Tarea con kwargs",
        "repeticiones": 4,
        "pausa": 0.7
    }
)

# Iniciar el hilo
hilo.start()
# Esperar a finalizar el hilo
hilo.join()

print("Fin")