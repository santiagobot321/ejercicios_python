#Pide dos valores al usuario e imprime los valores intercambiados.

# num1 = input("Introduce el primer número: ")
# num2 = input("Introduce el segundo número: ")

# num1,num2 = num2,num1

# print (f"Los números intercambiados son: {num1,num2}")







'''Pide un número de tres cifras (ej. 123) y muestra sus cifras en orden inverso (321).
💡 Usa operaciones matemáticas para extraer centenas, decenas y unidades.'''

# num = int(input("Escribe un numero de tres cifras: "))

# #Centenas
# conv = num//100

# #Decenas
# conv1 = (num-100*conv)//10

# #Unidades
# conv2 = num-100*conv-10*conv1

# #Convertimos los números a strings para poder imprimirlos en el orden contrario
# finalnum = str(conv2) + str(conv1) + str(conv)

# print(finalnum)




'''Extraer hora, minuto y segundo de segundos totales
Pide al usuario un número de segundos y muestra cuántas horas, minutos y segundos son.'''

segundos = float(input("Digite los segundos: "))



