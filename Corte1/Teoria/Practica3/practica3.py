cond = True #Inicializa condicion del bucle general
cond2 = True #Inicializa Condicion del bucle de condicion de salida

while cond:
    a = input("Por favor ingrese un valor: ") #Solicita ingresar numero

    aInt = int(a) #Convierte a entero
    mod = aInt%2 #Calcula el modulo

    if (mod == 0):
        print("El número es par") #Imprime respuesta en caso de par
    else:
        print("El número es impar") #Imprime respuesta en caso de impar

    while cond2:
        question = input("Desea continuar? (S/N): ") #Solicita ingresar condicion de salida
        if (question == 'S'):
            cond = True #Continua ejecutando el programa
            cond2 = False #Deja de preguntar por condicion de salida
        elif (question == 'N'):
            cond = False #Deja de ejecutar el programa
            cond2 = False #Deja de preguntar por condicion de salida
        else:
            print("Comando no reconocido") #Indica que no reconoce la respuesta a la condicion de salida
            cond2 = True #Continua preguntando por la condicion de saida

    cond2 = True #En caso de continuar ejecutando el programa garantiza seguir preguntando la condicion
                 #de salida
