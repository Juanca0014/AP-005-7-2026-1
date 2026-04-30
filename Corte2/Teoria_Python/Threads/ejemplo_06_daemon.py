import threading
import time

# Función target del hilo
def monitorear():
    while True:
        print("Monitoreando...")
        time.sleep(1)

# Crea el hilo como daemon
# daemon=true hace que aunque el hilo no termine el programa pueda finalizar
# Si el programa termina el hilo daemon termina abruptamente
hilo = threading.Thread(target=monitorear, daemon=True)

# Inicia el hilo
hilo.start()

# Actividad en el hilo principal
for i in range(5):
    print(f"Programa principal: {i}")
    time.sleep(1)

print("Fin del programa principal")
