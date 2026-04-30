import threading
contador = 0 # variable global

# Funcion target
def incrementar():
    global contador # Declarar variable como global
                    # Como ambos threads pueden modifica la variable al tiempo
                    # puede generar inconsitencias en la operacion
    for _ in range(100000):
        contador += 1

# Crea hilos
hilo_1 = threading.Thread(target=incrementar)
hilo_2 = threading.Thread(target=incrementar)

# Inicia el hilo
hilo_1.start()
hilo_2.start()

# Espera el fin del hilo
hilo_1.join()
hilo_2.join()

print("Contador final:", contador)