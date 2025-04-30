# #Pedimos la cantidad de kilometros a convertir
# cantidad = float(input("Escribe la cantidad de km a convertir: "))


# #Definimos los cálculos para las diferentes conversiones
# metros = cantidad*1000
# centimetros = cantidad*100000
# milimetros = cantidad*1000000

# print(f'{cantidad} KM = {metros:.2f} metros | {centimetros:.2f} centímetros | {milimetros:.2f} milímetros')





#__________________________________________________________________________________________________________________________________________________________

#pedimos los segundos

# seg = float(input('Ingresa la cantidad de segundos: '))


#Hacemos los respectivos calculos
# horas = seg//3600
# min = seg%3600
# minutos = min//60
# secu = seg%60
# segundos = min//60


#Imprimimos la respuesta
# print(f'\n{seg} segundos son: {horas} horas {minutos} minutos {secu} segundos')





#____________________________________________________________________________________________________________________________________________________________





# "Pide dos números y verifica si el primero es múltiplo del segundo usando %."

# num1 = int(input("Escribe el primer número: "))
# num2 = int(input("Escribe el segundo número: "))

# if num2%num1 == 0:
#     print(f"{num2} es múltiplo de {num1}")
# else:
#     print(f"{num2} no es múltiplo de {num1}")







#____________________________________________________________________________________________________________________________________________________________






# 🧮 Calculadora de salario neto

# Pide:

#     Sueldo bruto
#     Porcentaje de descuento (por ejemplo: 13)

# Calcula el sueldo neto usando la fórmula:

#     sueldo_neto = sueldo_bruto - (sueldo_bruto * descuento / 100)


# print("Calculadora")

# sueldo = int(input("Escribe tu sueldo bruto: "))
# descuento = float(input("Escribe el porcentaje de descuento: "))

# sueldo_neto = sueldo - (sueldo*descuento/100)

# print(f"El sueldo neto es: {sueldo_neto:.2f}")


#____________________________________________________________________________________________________________________________________________________________




# ⏳ Años para jubilarse

# Pide la edad y el género del usuario ("M" para mujer, "H" para hombre).

#     Mujer se jubila a los 60 años
#     Hombre se jubila a los 65 años

# Si ya se puede jubilar, muestra un mensaje celebratorio.
# Si no, indica cuántos años faltan para la jubilación.


# edad = int(input("Escribe tu edad: "))
# genero = str(input("Escribe tu género: "))

# if edad >= 65 and (genero.upper() == "M" or "H"):
#     print("¡Felicitaciones! ya puedes jubilarte")
# elif 0 <= edad < 60 and genero.upper() == "M":
#     print(f"Edad de jubilación de las mujeres es de 60 años, aún te faltan {60 - edad} años para jubilarte.")
# else:
#     print(f"La edad de jubilación de los hombres es de 65 años. Aún te faltan {65 - edad} años para jubilarte")






#_____________________________________________________________________________________________________________________________________________________________


# 📊 Calculadora de promedio con validación

# Pide al usuario 3 notas (entre 0 y 10).

#     Si alguna nota está fuera del rango, muestra un mensaje de error.
#     Si todas son válidas, calcula el promedio y muestra si el estudiante aprueba (≥ 6) o reprueba.

numero_notas = int(input("¿Cuántas notas son? "))
lista = []
prom = 0
acum = 0
for i in range(numero_notas):
    nota = float(input(f"Escribe la nota {i+1} (0 / 10): "))
    while nota < 0 or nota > 10:
        print("Ingresa una nota correcta")
        nota = float(input(f"Escribe la nota {i+1} (0 / 10): "))
    lista.append(nota)
    acum += lista[i]
    prom = acum / numero_notas
    
if 0 < prom >= 6:
    print(f"Felicitaciones! Pasaste con {prom}")
else: 
    print(f"No pasaste, sacaste {prom}")