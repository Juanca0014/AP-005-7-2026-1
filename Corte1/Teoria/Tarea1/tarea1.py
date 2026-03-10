#------------LISTAS----------------------
# Crear lista de 6 posiciones
lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
# Imprimir lista
print(lista)
# Imprimir clase de la lista
print(type(lista))
# Imprimir posicion 2 de la lista
print(lista[2])

# Imprimir longitud de la lista
print("Tamaño de la lista: ", len(lista))
# Imprime elementos del 0 al 2 sin incluir el 2
print(lista[0:2])
# Imprime elementos de primer elemento al 2 sin incluir el 2
print(lista[:2])

# Agregar un nuevo elemento a la lista en el ultimo lugar
lista.append('Blanco')
# Imprimir la lista
print(lista)

# Agregar un nuevo elemento en la posicion 3 de la lista
lista.insert(3, 'Negro')
# Imprimir la lista
print(lista)

# Concatena otra lista al final de la primera
lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
# Imprimir en lista
print(lista)

# Señala la posicion donde esta el elemento buscado en la lista
print(lista.index('Azul'))

# Elimina un elemento de la lista y se re-indexa
lista.remove('Marron')
# Imprimir lista
print(lista)

# Insterar un elemento (El borrado) a la lista en la posicion 8 (Donde estaba antes)
lista.insert(8, 'Marron')
# Imprimir lista
print(lista)

# Elimina el ultimo (Por defecto) elemento de la lista y lo retorna
print(lista.pop())
# Longiitud de la lista
size = len(lista)
# Imprimir longitud de la lista
print("size = ", size)
# Imprimir el ultimo elemento de la lista
print(lista.pop(size-1))

# Multiplica la lista por 3, es decir se concatena con si misma 3 veces
lista_3 = lista*3
# Imprimir la lista concatenada
print("lista_3: ", lista_3)

# Ordena los elementos de la lista
print("Ordena:")
# listaSort = sort() # Esto no funciona porque .sort() retorna none
                     # y se almacena en la misma lista original
listaSort = sorted(lista) # sorted la ordena pero debe almacenarce en una nueva lista
# Imprime la lista
print(listaSort,"\n") # La lista se ordena en orden alfabetico

# Nueva lista de números del 10 al 1
NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
# Imprimir lista
print("Lista ordenada de menor a mayor: ")
# Ordenar la lista de menor a mayor
NumList.sort() # Ordena por defecto de menor a mayor
# Imprimir lista
print(NumList)

# Re-ordena la lista de mayor a menor
NumList.sort(reverse = True)
# Imprime la lista
print("Mayor a menor: ", NumList,"\n")



#-------------------TUPLAS------------------

# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

# Convertir una lista a tupla
print("############TUPLAS#########")
# Conierte la lista a tupla
tupla = tuple(lista)
print()
print()
# Imprime la tupla
print("tupla: ", tupla)

# Posición 0 de la tupla
print(tupla[0])
# Posición 2 de la tupla
print(tupla[2])


# Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in tupla)
# Cuenta cuantos de ese elemento hay en la tupla
print(tupla.count('Rojo'))

#Tupla con un solo elemento
tupla_unitaria = ('Blanco')
# Imprime la tupla
print(tupla_unitaria)

# Empaquetado de tupla, tupla sin paréntesis
tupla = 'Gaspar', 5, 8, 1999
# Imprime tupla
print(tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = tupla
# Imprime valores desempaquetados
print(nombre)
print(dia)
print(mes)
print(año)

# Imprime los valores concatenados con texto
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convertir una tupla en una lista
lista2=list(tupla)
# Imprimir nueva lista
print(lista2)