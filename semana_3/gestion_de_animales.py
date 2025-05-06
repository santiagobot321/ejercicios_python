nombres = []
edades = []
enfermo = []

def agregar():
  numanimales = int(input("¿Cuántos animales?: "))
  for i in range(numanimales):
    name = str(input("Ingresa el nombre del animal: "))
    age = int(input("Ingresa la edad del animal: "))
    sick = str(input("¿Está enfermo o sano?: ")).lower()
    nombres.append(name)
    edades.append(age)
    enfermo.append(sick)
  return nombres,edades,enfermo
    
def eliminar():
  nameeliminar = input("\nEscribe el nombre del animal que deseas eliminar: ")
  if nameeliminar in nombres:
    indice = nombres.index(nameeliminar)  
    del nombres[indice]
    del edades[indice]
    del enfermo[indice]
    print(f"\n\033[35m{nameeliminar} ha sido eliminado\033")
  else:
    print(f"\033[31m{nameeliminar} no se encuentra en la lista\033[0m")
  
def listar():
  for i in range(len(nombres)):
    print(f"\033[34m{nombres[i]}\033[0m | \033[32m{edades[i]}\033[0m | \033[32m{enfermo[i]}\033[0m")    


while True:
    print("\n                 \033[33mGestión de animales\033[0m\n",
      "\n 1) Agregar un animal\n",
      "2) Eliminar un animal por su nombre\n",
      "3) Listar todos los animales registrados\n",
      "4) Salir\n"
    )
    respuesta = int(input("Elige una de las opciones: "))
    
    match respuesta:
      case 1:
        agregar()
        
      case 2:
        eliminar()
        
      case 3:
        listar()
        
      case 4:
        print("\n\033[31mDeteniendo el flujo del programa...\033[0m\n")
        break