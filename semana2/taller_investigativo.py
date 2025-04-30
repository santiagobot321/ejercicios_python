#¿Qué es un array o lista en Python?

#     Investiga qué son los arrays (o listas) en Python y para qué se utilizan.
#     ¿Cómo se declara una lista vacía?
#     ¿Cómo se crea una lista con valores iniciales?

# Ejemplo práctico:

#     Crea una lista llamada mi_lista con los números del 1 al 5.

#____ SOLUCION _____#

# Un array es un contenedor con un número predefinido de valores de un determinado tipo

# Para declarar un arreglo en python se hace:

#arreglo = []

# Podemos ponerle al arreglo valores iniciales separándolos por comas:

#arreglo = [2,3,5,7,11,13]

# Creando un arreglo con los números del 1 al 5

#mi_lista = [1,2,3,4,5]


#     ¿Cómo se accede al primer elemento de una lista?
#     ¿Qué significa usar un índice negativo?
#     ¿Qué pasa si intento acceder a un índice que no existe?

# Ejemplo práctico:

#     Crea una lista [10, 20, 30, 40] y muestra el primer y el último elemento.

#____ SOLUCION _____#

#Para acceder a un elemento en concreto de la lista, podemos hacerlo de la siguiente manera, empieza desde el cero:

#print(mi_lista[0])


# Con indices negativos se obtienen los elementos en sentido contrario, empezando por el final
# for i in range(len(mi_lista)):
#     print(mi_lista[-i])
    

# Si intentamos acceder a una posición que no existe, nos arroja un error de "indice de la lista está fuera del rango"
# print(mi_lista[5])

'''''
¿Qué es el "slicing" o rebanado de listas?
    ¿Qué significa "slicing" en listas?
    ¿Cómo se obtiene una sublista usando slicing?
    ¿Qué significa dejar vacío el inicio o el final en el slicing?
''''' 

# ____ SOLUCION _____ #

# Slicing es una forma de extraer elementos de una secuencia 

#Para obtener una sublista con slicing

#valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(valores[0:5])

# Cuando se deja un espacio vacío, se da a entender que son todos los elementos que siguen despues de ahí
#print(valores[5:])

'''''
¿Cómo modificamos los elementos de una lista?

    ¿Cómo se cambia el valor de un elemento de la lista?
    ¿Qué pasa si modificamos un índice que no existe?

Ejemplo práctico:

    Cambia el tercer elemento de [10, 20, 30, 40] por 99.
'''''

#Para modificar elementos de una lista, se cambia por el que queramos usando la posición

# valores = [10,20,30,40]

# valores[2] = 99

# print(valores)

# # Si se pone con un indice que no existe, da que está fuera del rango

# valores [8] = 900 # IndexError: list assignment index out of range



 
# 5. ¿Cómo agregamos nuevos elementos a una lista?

#     ¿Cómo se agrega un elemento al final de la lista?
#     ¿Cómo se inserta un elemento en una posición específica?
#     ¿Cómo se combinan dos listas en una sola?

# Ejemplo práctico:

#     A una lista [10, 20, 30] agrega:
#         El número 40 al final.
#         El número 15 en la posición 1.
#         Los números 50 y 60 al final de la lista.

# Para agregar elementos al final, se usa el método .append()

# Para agregarlo en una posición específica se usa el método insert

# lista = [10,20,30]

# lista.append(40)
# lista.insert(0,15)
# lista.append(50)
# lista.append(60)

# print(lista)


# 6. ¿Cómo eliminamos elementos de una lista?

#     ¿Cómo se elimina un valor específico de una lista?
#     ¿Qué hace el método pop()?
#     ¿Cómo se elimina un elemento usando del?

# Ejemplo práctico:

#     De la lista [10, 20, 30, 40, 50], realiza las siguientes acciones:
#         Elimina el número 30.
#         Elimina el último elemento.
#         Elimina el segundo elemento (índice 1).


# _______ SOLUCION ________ #

#Eliminamos con el método pop

#Usamos "del" de la siguiente manera: del mi_lista[0] y eso elimina el primer elemento

# lista = [10,20,30,40,50]

# lista.pop(2)
# lista.pop(3)
# del lista[1]
# print(lista)


# 7. ¿Cómo buscamos elementos dentro de una lista?

#     ¿Cómo se verifica si un elemento está presente en una lista?
#     ¿Cómo encontrar el índice de un elemento?
#     ¿Cómo contar cuántas veces aparece un valor en la lista?

# Ejemplo práctico:

#     Con la lista [10, 20, 30, 40, 50]:
#         Verifica si el número 20 está en la lista.
#         Encuentra el índice del número 30.
#         Cuenta cuántas veces aparece el número 20.


# _____ SOLUCION ______ #

# Se verifica si un elemento está dentro de una lista usando un for y un if
# Para encontrar el indice se usa .index
# Para contar se puede usar un contador junto con un for e if o con el método count

# lista = [10, 20, 30, 40, 50]

# for i in lista:
#     if i == 20:
#         print("Sí está")

# print(lista.index(30))

# print(lista.count(20))


# 8. ¿Cómo ordenamos los elementos de una lista?

#     ¿Cómo se ordena una lista de manera ascendente?
#     ¿Cómo se ordena en orden descendente?
#     ¿Qué diferencia hay entre sort() y sorted()?

# Ejemplo práctico:

#     Ordena la lista [40, 10, 30, 20]:
#         Primero en orden ascendente.
#         Luego en orden descendente.
#         Crea una nueva lista ordenada sin modificar la original.

# _______ SOLUCION ______ #

# para ordenar lista se hace con .sort()

# para ordenar de manera descendente se hace con .sort(inverse = true)

# sorted() da una nueva lista ordenada, en cambio sort modifica la ya existente

 
# lista = [40, 10, 30, 20]

# lista.sort()

# print(lista)

# lista.sort(reverse=True)

# print(lista)

# print(sorted(lista))


# 9. ¿Cómo invertimos el orden de los elementos de una lista?

#     ¿Cómo invertir una lista usando reverse()?
#     ¿Cómo invertir una lista usando slicing?

# Ejemplo práctico:

#     Invierte el orden de [10, 20, 30, 40] utilizando ambas técnicas.

# __________ SOLUCION _________ #

# lista = [10, 20, 30, 40]

# # lista.reverse()

# # print(lista)

# print(lista[::-1])


# 10. ¿Cómo hacemos una copia de una lista?

#     ¿Cómo copiar una lista usando slicing?
#     ¿Cómo copiarla usando list()?
#     ¿Cómo copiarla usando copy()?

# Ejemplo práctico:

#     Copia la lista [10, 20, 30] de tres maneras diferentes.


# Copiar una lista con slicing nueva_lista = lista[:]

# Usando list sería nueva_lista = list(lista)

# Usando copy sería nueva nueva_lista = lista.copy()

# lista = [10, 20, 30]

# print(lista[:])

# nuevalista = list(lista)

# print(nuevalista)

# nueva_lista = lista.copy()

# print(nueva_lista)


# 11. ¿Cómo comprobamos si una lista está vacía?

#     ¿Cómo podemos saber si una lista no tiene elementos?

# Ejemplo práctico:

#     Crea una lista vacía y escribe un código que imprima "La lista está vacía" si no contiene datos.


#___ SOLUCION ____ #

# Podemos mirar si una lista tiene elementos con len()

# lista = []
# if len(lista) == 0:
#     print("La lista está vacía")


# 12. ¿Cómo pedir varios datos al usuario y almacenarlos en una lista?

#     ¿Cómo pedimos al usuario la cantidad de datos que quiere ingresar?
#     ¿Cómo almacenamos esos datos en una lista usando un ciclo for?

# Ejemplo práctico:

#     Escribe un programa que:
#         Pregunte al usuario cuántos elementos quiere ingresar.
#         Luego pida esos elementos uno por uno.
#         Finalmente, muestre la lista completa.


#_____ SOLUCION _______ #

# Para manejar los datos del usuario usamos un input()
# Los almacenamos en una lista con .append()

# elementos = int(input("¿Cuántos elementos quiere ingresar?: "))
# lista = []
# for i in range(elementos):
#     dato = int(input("ingrese el dato: "))
#     lista.append(dato)
# print(lista)