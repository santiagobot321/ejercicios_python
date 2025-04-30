print("Primero llenemos las calificaciones")

# Inicializamos las variables

lista_cali = []
acum = 0
cont = 0
contador = 0

# Rellenamos la lista con la cual operaremos 
numero_cali = int(input("\n¿Cuántas calificaciones son?: "))
for i in range(numero_cali):
    calificaciones = float(input("Ingresa las calificaciones: "))
    lista_cali.append(calificaciones)
    #Acumulamos la suma de las calificaciones
    acum += lista_cali[i]

#Mostramos el menú de opciones
while True:
    print("\n¿Qué deseas hacer? Escoje una opción: \n",
        "1) Determinar el estado de aprobación: \n",
        "2) Calcular el promedio: \n", 
        "3) Contar calificaciones mayores: \n",
        "4) Verificar y contar calificaciones específicas \n",
        "5) Salir del programa\n")
    respuesta = int(input("Elige una de las opciones: "))

# Dependiendo de la elección, se da un caso u otro con un match - case
    match respuesta:
        #Si escogemos 1, hará la comparación con la nota que le ingresamos
        case 1:
            
            calificacion = float(input("Ingresa una calificación del 1 - 100: "))
            if calificacion >= 65:
                print("\n\033[32mFelicidades, está aprobado\033[0m\n")
            else:
                print("\n\033[31mReprobado\n\033[0m")
        
        case 2:
            #Si escogemos 2, calculará el promedio de las notas ingresadas
            promedio = acum / numero_cali
            print(f"\n\033[32mTu promedio es {promedio}\033[0m")
            
        case 3:
            #Si esogemos 3, recorrerá la lista con el for en busca de las calificaciones que sean mayores a la ingresada
            valor_especifico = float(input("Ingresa un valor a comparar: "))
            for i in lista_cali:
                if i > valor_especifico:
                    cont += 1
            print(f"\033[32m{cont} calificaciones son mayores que este valor\033[0m")
        
        case 4:
            #Si escogemos 4, compararemos con un while cada elemento de la lista, buscando por número repetidos. En caso de que no lo encuentre
            # sumará uno al iterador y continuará con la siguiente posición. Si en dicha posición encuentra el número, suma uno al contador.
            calificacion_especifica = float(input("Escribe una calificación específica a contar: "))
            i = 0
            
            while i < len(lista_cali):
                if lista_cali[i] != calificacion_especifica:
                    i+=1
                    continue
                cont +=1
                i+=1
                
            print(f"\033[32mLa calificación se repite {cont} veces\033[0m")
            
        case 5:
            print("\033[31mSaliendo del programa...\033[0m")
            break
                
            
#PD: Se usaron códigos de secuencia ANSI para colorear la salida y dar mayor legibilidad.