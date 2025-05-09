# Creamos el diccionario
productos = {}

# Definimos las funciones para la parte de validaciones
def input_str(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:  # Verifica que la entrada no esté vacía
            return dato
        print("\033[31mError: Ingresa un texto válido.\033[0m")

# Que sea flotante
def input_float(mensaje):
    dato = float(input(mensaje))
    if dato > 0:
        return dato
    else:
        print("\033[31mError: Ingresa un número positivo\033[0m")
    print("\033[31mError: Ingresa un texto válido.\033[0m")

# Que sea entero
def input_int(mensaje):
    dato = int(input(mensaje))
    if dato > 0:
        return dato
    else:
        print("\033[31mError: Ingresa un número positivo\033[0m")
    print("\033[31mError: Ingresa un texto válido.\033[0m")

# Definimos la primera función para añadir productos
def add_product():
        
        # Pedimos los datos
        product_name = input_str("Ingresa el nombre del producto: ")
        product_price = input_float("Ingresa el precio del producto: ")
        product_quantity = input_int("Ingresa la cantidad de productos disponible: ")
        # Asignamos al nombre del producto como valor una tupla con el precio y la cantidad del producto 
        productos[product_name] = (product_price,product_quantity)
        print(f"""               
              \033[34m{product_name} ha sido añadido exitosamente.\033[0m
                            
              Su precio es: \033[32m${productos[product_name][0]}\033[0m y su cantidad es: {productos[product_name][1]}
              """)
        
# Definimos la funcion para buscar los productos por el nombre
def search_product():
    producto_name = input_str("Ingresa el nombre del producto a consultar: ")
    # Hacemos la validación de si el nombre está en el diccionario
    if producto_name in productos:
        print(f"""
              
              El producto \033[31m{producto_name}\033[0m tiene un precio de \033[32m${productos[producto_name][0]}\033[0m
              y hay una cantidad de \033[33m{productos[producto_name][1]}\033[0m""")

# Definimos la función para actualizar el producto      
def update_product():
    producto_name = input_str("Ingresa el nombre del producto: ")
    # Hacemos de nuevo la validación
    if producto_name in productos:
        nuevo_precio = input_float("Ingresa el nuevo precio: ")
        # Como una tupla no se puede modificar, creamos de nuevo una lista y la reasignamos nuevamente
        productos[producto_name]= (nuevo_precio,productos[producto_name][1])
    print(f"""
          
          El precio de {producto_name} ha sido actualizado correctamente
          
          """)

# Definimos la función para eliminar     
def del_product():
    producto_name = input_str("Ingresa el nombre del producto a eliminar: ")
    if producto_name in productos:
        # Usamos del para eliminar todo lo relacionado al producto 
        del productos[producto_name]
    print(f"""
          El producto {producto_name} ha sido eliminado correctamente
          """)
# Definimos la función lamda que suma todos los productos por sus cantidades.
# Accedemos a la posición del precio y lo multiplicamos por el número de la posición del producto 
suma = lambda : sum(productos[i][0] * productos[i][1]for i in productos)


# Con un ciclo while hacemos el menú
while True:
    print("""
          
          1) Añadir productos
          2) Consultar productos
          3) Actualizar precios
          4) Eliminar productos
          5) Calcular valor total del inventario
          6) Salir
          
          """)
    # Finalmente recibimos la opción y la validamos con un match case 
    opcion = int(input("Elige una opción: "))
    match opcion:
            case 1:
                add_product()
            case 2:
                search_product()
            case 3:
                update_product()
            case 4:
                del_product()
            case 5:
                print(f"\n\033[33mEl precio total del inventario es {suma()}\033[0m")
            case 6:
                print("\n\033[34mSaliendo...\033[0m")
                break
            case _:
                ("Elija una opción válida del 1 al 6")
               

