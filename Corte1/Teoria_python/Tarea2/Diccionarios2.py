## Puedes acceder a los valores en un diccionario dando la clave

## Crea diccionario
#building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
## Imprime el valor asociado a la clave "Burj Khalifa"
#print(building_heights["Burj Khalifa"]) # Prints 828
## Imprime el valor asociado a la clave "Ping An"
#print(building_heights["Ping An"]) # Prints 599

## Crea un diccionario de los signos del zodiaco y les asigna como clave su elemento
#zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
## Imprime los signos de elemento tierra
#print(zodiac_elements["earth"])
## Imprime los signos de elemento fuego
#print(zodiac_elements["fire"])

## Ingresar clave equivocada
#building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#print(building_heights["Landmark 81"])
## Al intentar llamar una clave que no existe en ese diccionario genera
## el error: KeyError 'clave erronea'

## Una forma de evitar este error es primero revisar si la clave existe en el diccionrio:
#key_to_check = "Landmark 81"
## En caso de existir imprime, en caso contrario no
#if key_to_check in building_heights:
#    print(building_heights["Landmark 81"])

## Crea un diccionario
#zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
## Añade la clave "energy" emparejada al valor "Not a zodiac element"
#zodiac_elements["energy"] = "Not a Zodiac element"
## Si la clave existe aclara que no es un elemento
#if "energy" in zodiac_elements:
#   print(zodiac_elements["energy"])

## Obtener una clave de manera segura
## Nuevo diccionario
#building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

## Obtiene el valor asignado a "Shangai Tower"
#building_heights.get("Shanghai Tower")

## No obtiene nada porque "My House" no pertenece al diccionario
## Evita el error al buscar claves que no existen
#building_heights.get("My House")

## Crea un nuevo diccionario
#user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
## Obtiene una valor
#user_ids.get("teraCoder")

## Si el ususario no existe almacena 1000 si lo hace almacena el valor asociado en tc_id
#if user_ids.get("teraCoder") == None:
#   tc_id = 1000
#else: 
#   tc_id = user_ids.get("teraCoder")

## Imprime el resultado de la operacion anterior
#print(tc_id)

## Reptie el proceso con otra clave
#if user_ids.get("superStackSmash") == None:
#     stack_id = 100000

#print(stack_id)

## Eliminar una clave
## .pop() funciona para borrar items de un diccionario, cuando se sabe el valor y clave.
#raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
## Imprime el valor asociado a esa clave
#print(raffle.pop(320291, "No Prize"))
## Imprime el diccionario tras borrar el item con la clave ingresada en .pop()
#print(raffle)
## Al no exisitir esa clave imprime "No Prize"
#print(raffle.pop(100000, "No Prize"))
## Imprime el diccionario sin modificaciones pues no se borro nada al no existir
#print(raffle)
## Imprime el valor asociado a esa clave
#print(raffle.pop(872921, "No Prize"))
## Imprime el diccionario tras borrar el item con la clave ingresada en .pop()
#print(raffle)

## Crea un diccionario con valores de item consumibles
#available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
## Establece una variable de valor de vida
#health_points = 20

## Suma el valor de uno de los items y lo elimina del diccionario
#health_points += available_items.pop("stamina grains", 0)
#health_points += available_items.pop("power stew", 0)
#health_points += available_items.pop("mystic bread", 0)

## Imprime los items restantes en el diccionario
#print(available_items)
## Imprime la vida actual
#print(health_points)

## obtener todas las claves
#test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
## Imprime una lista de las claves
#print(list(test_scores))

## Recorre el diccionario
#for student in test_scores.keys():
#  print(student)

## Crea dos diccionarios
#user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
#num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

## Obtiene las claves
#users = user_ids.keys()
#lessons = num_exercises.keys()

## Imprime las claves
#print(users)
#print(lessons)

## Obtener los valores
## Crea un nuevo diccionario
#test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

## Imprime los valores para cada clave
#for score_list in test_scores.values():
#  print(score_list)

## Crea un nuevo diccionario
#num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
## Crea una variable con el total de ejercicios
#total_exercises = 0

## Recorre el diccionario y acumula los valores en una variable
#for exercises in num_exercises.values():
#   total_exercises += exercises
#   print(total_exercises)

## Obtener todos los items
## Crea un nuevo diccionario
#biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

## Recorre el diccionario e imprime las claves concatenadas a sus valores
#for company, value in biggest_brands.items():
#  print(company + " has a value of " + str(value) + " billion dollars. ")

## Crea un nuevo diccionario
#pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

## Recorre el diccionario e imprime las claves concatenadas a sus valores
#for occupation, percentage in pct_women_in_occupation.items():
#   print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 