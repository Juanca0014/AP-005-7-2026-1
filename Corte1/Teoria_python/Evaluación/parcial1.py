# Tupla con categorías fijas del sistema
CATEGORIAS = ("Libros", "Peliculas", "Videojuegos", "Electrodomesticos", "Otros")
# Lista donde se almacenan los productos
# 2 productos de prueba
inventario = [
    {
        "codigo": 1,
        "nombre": "Dune",
        "precio": 50000.0,
        "cantidad": 10,
        "categoria": "Libros"
    },
    {
    "codigo": 2,
        "nombre": "Disco Elysium",
        "precio": 60000.0,
        "cantidad": 5,
        "categoria": "Videojuegos"
    }
]
################################################
# Funcion del menú: Imprime el menú
def menu():
    print("\n########## MENÚ ##########")
    opciones = [
        "1. Agregar producto",
        "2. Mostrar productos",
        "3. Buscar producto",
        "4. Eliminar producto",
        "5. Salir"
    ]
    for op in opciones:
        print(op)
################################################
# Funcion de agregar productos: Agrega los productos como diccionarios
#                               a la lista del inventario
def agregar():
    print("\n--- Agregar Producto ---")
    
    # Validacion de tipo de dato
    try: #prueba la conversion de datos a entero, sino  es retorna la funcion
        codigo = int(input("Ingrese código: "))
    except:
        print("Error: El codigo debe ser un número entero")
        return
    
    # Validación de duplicado/coincidencia

    if any(item["codigo"] == codigo for item in inventario):
        print("Error: El código ya existe.")
        return
    
    nombre = input("Ingrese nombre: ")
    
    # Validacion de tipo de dato
    try: #prueba la conversion de datos a float, sino  es retorna la funcion
        precio = float(input("Ingrese precio: "))
    except:
        print("Error: precio debe ser un numero con punto decimal.")
        return
    
    # Validacion de tipo de dato
    try: #prueba la conversion de datos a entero, sino  es retorna la funcion
        cantidad = int(input("Ingrese cantidad: "))
    except:
        print("Error: La cantidad debe ser un número entero")
        return

    print("Categorías disponibles:", CATEGORIAS)
    categoria = input("Ingrese categoría: ")
    
    # Validacion de categoria: existe en la tupla/datos fijos
    if categoria not in CATEGORIAS:
        print("Categoría no válida.")
        return
    
    #Diccionarios
    item = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }
    
    # Agrega nueva fila a la lista
    inventario.append(item)
    print("Producto agregado correctamente.")
################################################
# Funcion de mostrar productos: Reorganiza la lista y la imprime
def mostrar():

    print("\n--- Lista de Productos ---")
    
    if not inventario:
        print("No hay productos registrados.")
        return
    
    # Ordena una nueva lista y la imprime
    inventario_ordenado = sorted(inventario, key=lambda item: item["codigo"])

    for item in inventario_ordenado:
        print(f"Código: {item['codigo']}, Nombre: {item['nombre']}, "
              f"Precio: {item['precio']}, Cantidad: {item['cantidad']}, "
              f"Categoría: {item['categoria']}")
################################################
# Funcion de buscar producto: Recorre la lista y imprime el producto
#                             con el codigo especificado
def buscar():
    print("\n--- Buscar Producto ---")
    
    try: #prueba la conversion de datos a entero, sino  es retorna la funcion
        codigo = int(input("Ingrese código a buscar: "))
    except:
        print("Error: El codigo debe ser un número entero")
        return
    
    # Recorre la lista buscando la coincidedncia del codigo
    for item in inventario:
        if item["codigo"] == codigo:
            print("Producto encontrado:")
            print(f"Código: {item['codigo']}, Nombre: {item['nombre']}, "
                  f"Precio: {item['precio']}, Cantidad: {item['cantidad']}, "
                  f"Categoría: {item['categoria']}")
            return
    
    print("Producto no encontrado.")
################################################
# Funcion eliminar producto: Elimina de la lista el producto con el codigo
#                            especificado
def eliminar():
    print("\n--- Eliminar Producto ---")
    
    try: #prueba la conversion de datos a entero, sino  es retorna la funcion
         codigo = int(input("Ingrese código a eliminar: "))
    except:
        print("Error: El codigo debe ser un número entero")
        return
    
    # Recorre la lista buscando la coincidencia del codigo
    for item in inventario:
        if item["codigo"] == codigo:
            # Borra el producto que tiene la coincidencia
            inventario.remove(item)
            print("Producto eliminado.")
            return
    
    print("Producto no encontrado.")
################################################
# Programa principal
print("\nBienvenido al sistema de inventario de la tienda de Camilo")

while True:
    input("\ncontinuar...")
    menu()
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        buscar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")

print("Gracias por ingresar")