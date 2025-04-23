# Solicitar al usuario los datos del producto

nombre_producto = input("Ingresa el nombre del producto: ")
precio_producto = float(input("Ingresa el precio del producto: "))
cantidad_producto = int(input("Ingresa la cantidad del producto: "))
descuento = float(input("Ingresa el descuento del producto: "))

# Validamos que se ingresen valores correctos

if precio_producto > 0 and cantidad_producto > 0 and 0 <= descuento <= 100 and nombre_producto != "":
    
    # Calculamos el costo total
    
    costototal1 = precio_producto*cantidad_producto
    
    print(f"El costo total de {nombre_producto} es: {costototal1:.2f}")
    
    # Una vez ingresados los datos correctamente, si los datos se ingresan correctamente y el descuento es mayor a cero, se hace el cálculo total
    
    if descuento > 0:

        # Como el descuento es mayor a cero, se le resta al acumulado del costo total 

        costototal1 -= costototal1*(descuento/100)

        print(f"el precio total de {nombre_producto} es: {costototal1:.2f}")   
else:
        
        # Si el usuario ingresa mal los datos, le envia un mensaje de error
        
        print("Ingresa un valor válido en todos los campos")

