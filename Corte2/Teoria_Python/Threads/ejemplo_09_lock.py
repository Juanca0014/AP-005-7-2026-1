import threading
contador = 0                # Crea variable global
candado = threading.Lock()  # Crea bloqueo de modificacion entre multiples hilos

# Función target
def incrementar():
    global contador         # Declara la variable global
    for _ in range(100000):
        with candado:       # Permite la modificación si y solo si otro thread no la esta utilizando
                            # Se recomiendo proteger solo la parte necesaria como la modificacion de la variable global
            contador += 1

# Crea los hilos
hilo_1 = threading.Thread(target=incrementar)
hilo_2 = threading.Thread(target=incrementar)

# Inicia los hilos
hilo_1.start()
hilo_2.start()

# Espera el fin de los hilos
hilo_1.join()
hilo_2.join()

print("Contador final:", contador)