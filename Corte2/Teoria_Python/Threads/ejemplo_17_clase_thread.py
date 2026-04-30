import threading
import time

class Contador(threading.Thread):
    # Las definiciones del hilo y atributos
    def __init__(self, nombre, limite):
        super().__init__()
        self.nombre = nombre
        self.limite = limite

    # Lo que hará el hilo, no se llama directamente, se llama con .start()
    def run(self):
        for i in range(self.limite):     # Utiliza el atributo de limite
            print(f"{self.nombre}: {i}") # Utiliza el atrubuto de nombre
            time.sleep(1)

# Crea hilos segun la clase
contador_a = Contador("Contador A", 5)
contador_b = Contador("Contador B", 5)

# Inicia hilo
contador_a.start()
contador_b.start()

# espera final del hilo
contador_a.join()
contador_b.join()

print("Fin")