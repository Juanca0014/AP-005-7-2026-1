## Diccionarios -> clave:valor
## Crea un nuevo diccionario "sensors"
#sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
## Crea un nuevo diccionario "num_cameras"
#num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

## Imprime ambos diccionarios
#print(sensors)
#print(num_cameras)

## Crea un nuevo diccionario de elementos de texto
## funcionaria como un traductor a un idioma ficticio
#translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
## Imprime el diccionario
#print(translations)

## Verificar un error:
## Retorna la advertencia de que una clave no puede ser una lista
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# print(powers)

## Por el contrario una clave si puede estar asociada a una lista de valores
#children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
#print(children)

## Se crea un diccionario vacio y se imprime "{}" vacio
#my_empty_dictionary = {}
#print(my_empty_dictionary)

## Se crea un nuevo diccionario
#menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
## Se imprime el nuevo diccionario
#print("Before: ", menu)
## Agregar cheesecake a final del diccionario
#menu["cheesecake"] = 8
## Imprime el diccionario cambiado
#print("After", menu)
## Crea un nuevo diccionario y lo sobreescribe
#animals_in_zoo = {"dinosaurs": 0}
#animals_in_zoo = {"dinosaurs": 0}
#animals_in_zoo = {"horses": 2}
## Imprime el diccionario que solo va a contener la ultima sobreescritura
#print(animals_in_zoo)


## Añadir multiples claves:
## Crear un nuevo diccionario
#sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
## Imprime el nuevo diccionario
#print("Before", sensors)

## Actualiza el diccionario
#sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
## Imprime el diccionario actualizado con las nuevas entradas
#print("After", sensors)

## Añadir multiples entradas:
#user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
#print(user_ids)
#user_ids.update({"theLooper": 138475, "stringQueen": 85739})
#print(user_ids)

## Sobreescribir valores
## Sabemos que se puede añadir una nueva clave con la sintaxis:
## menu["banana"] = 3
## Crear el diciconario
#menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
## Imprimir el diccionario
#print("Before: ", menu)
## Sobreescribe el valor asociado a la clave "oatmeal" con la sintaxis sugerida
#menu["oatmeal"] = 5
## Imprime el diccionario
#print("After", menu)
## El valor de la clave "oatmeal" cambio

##Crea un nuevo diccionario
# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
##Imprime el diccionario
# print("Before", oscar_winners)
# print()
##Agrega nueva clave
# oscar_winners.update({"Supporting Actress": "Viola Davis"})
# print("After1", oscar_winners)
# print()
##Sobreescribe el valor de la clave "Best Picture"
# oscar_winners["Best Picture"] = "Moonlight"
# print("After2", oscar_winners)


## Comprension de diccionarios
## Digamos que tienes dos listas que quieres combinar en un
## diccionario,como una lista de estudiantes y una lista de sus
## alturas en pulgadas:

## Lista de nombres
#names = ['Jenny', 'Alexus', 'Sam', 'Grace']
## Lista de alturas
#heights = [61, 70, 67, 64]

##Python te permite crea un diccionario como
##una compresion de diccionario con esta sintaxis:

## Compresion de las listas en un objeto zip
#zipStudents = zip(names, heights)
## Imprimir la compresion
#print("zipStudents: ", zipStudents)

## Sintaxis para pasar el comprimido a key:value donde key <-names y value <-heights
#students = {key:value for key,value in zip(names,heights)}
## students ahora es: {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
## Imprime el nuevo diccionario
#print(students)

## zip() Combina dos listas en un iterador de tuplas con la
## lista de elementos emparejados juntos.

## Ejemplo 1 de compresion:
# drinks = ["espresso", "chai", "decaf", "drip"]
# caffeine = [64, 40, 0, 120]

# zipped_drinks = zip(drinks, caffeine)
# print(zipped_drinks)

# drinks_to_caffeine = {key:value for key, value in zipped_drinks}
# print(drinks_to_caffeine)

## Crea dos listas
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
## Comprime en un solo diccionario
plays = {key:value for key, value in zip(songs, playcounts)}
## Imprime el diccionario
print(plays)
## Añade una nueva clave
plays.update({"Purple Haze": 1})
## Sobreescribe un valor
plays.update({"Respect": 94})
## Imprime los cambios
print("After: ", plays)
## Concatena diccionarios
library = {"The Best Songs": plays, "Sunday Feelings": {}}
## Imprime la nueva biblioteca de diccionarios
print(library)