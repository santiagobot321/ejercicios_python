
productos = {}

def input_str(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:  # Verifica que la entrada no esté vacía
            return dato
        print("\033[31mError: Ingresa un texto válido.\033[0m")
        
def input_float(mensaje):
    dato = float(input(mensaje))
    if dato > 0:
        return dato
    else:
        print("\033[31mError: Ingresa un número positivo\033[0m")
    print("\033[31mError: Ingresa un texto válido.\033[0m")

def input_int(mensaje):
    dato = int(input(mensaje))
    if dato > 0:
        return dato
    else:
        print("\033[31mError: Ingresa un número positivo\033[0m")
    print("\033[31mError: Ingresa un texto válido.\033[0m")

def add_product():
        product_name = input_str("Ingresa el nombre del producto: ")
        product_price = input_float("Ingresa el precio del producto: ")
        product_quantity = input_int("Ingresa la cantidad de productos disponible: ")
        productos[product_name] = {"Precio":product_price,"Cantidad":product_quantity}
        print(f"""               
              \033[34m{product_name} ha sido añadido exitosamente.\033[0m
                            
              Su precio es: \033[32m${productos[product_name]["Precio"]}\033[0m y su cantidad es: {productos[product_name]["Cantidad"]}
              """)
        
def search_product():
    producto_name = input_str("Ingresa el nombre del producto a consultar: ")
    if producto_name in productos:
        print(f"""
              
              El producto \033[31m{producto_name}\033[0m tiene un precio de \033[32m${productos[producto_name]["Precio"]}\033[0m
              y hay una cantidad de \033[33m{productos[producto_name]["Cantidad"]}\033[0m""")
        
def update_product():
    producto_name = input_str("Ingresa el nombre del producto: ")
    if producto_name in productos:
        nuevo_precio = input_float("Ingresa el nuevo precio: ")
        productos[producto_name]["Precio"] = nuevo_precio
    print(f"""
          
          El precio de {producto_name} ha sido actualizado correctamente
          
          """)
    
def del_product():
    producto_name = input_str("Ingresa el nombre del producto a eliminar: ")
    if producto_name in productos:
        del productos[producto_name]
    print(f"""
          El producto {producto_name} ha sido eliminado correctamente
          """)

suma = lambda : sum(i["Precio"] * i["Cantidad"] for i in productos.values())

while True:
    print("""
          
          1) Añadir productos
          2) Consultar productos
          3) Actualizar precios
          4) Eliminar productos
          5) Calcular valor total del inventario
          6) Salir
          
          """)
    try:
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
                
    except ValueError:
        print("\033[31mError: Ingresa un número entre 1 y 6.\033[0m")
        
