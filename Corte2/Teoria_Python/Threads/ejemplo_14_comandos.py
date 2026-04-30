import threading
import time

detener = threading.Event()
estado = {"contador": 0}


def trabajo_en_segundo_plano():
    # Funciona mientras no haya eventosali
    while not detener.is_set():
        estado["contador"] += 1
        print(f"Contador interno: {estado['contador']}")
        time.sleep(1)

hilo = threading.Thread(target=trabajo_en_segundo_plano)
hilo.start()

while True:
    # Espera entrada
    comando = input("Escribe ’salir’ para terminar: ")    
    #Condicion de salida
    if comando.lower() == "salir":
        detener.set()
        break
        
    print(f"Comando recibido: {comando}")

# Espera final de hilo
hilo.join()

print("Programa finalizado")