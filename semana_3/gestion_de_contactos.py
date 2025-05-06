# Ejercicio: Gestión de Contactos
# Objetivo:

# Crear un diccionario para gestionar los contactos, donde la clave sea el nombre del contacto y el valor sea su número de teléfono. 
# El programa permitirá agregar nuevos contactos.
# Instrucciones:

#     Crea un diccionario llamado contactos donde cada clave sea el nombre de un contacto y su valor sea el número de teléfono.

#     El programa debe permitir al usuario realizar las siguientes operaciones:
#         Agregar un nuevo contacto (nombre, número de teléfono).
#         Mostrar todos los contactos almacenados.
#         Buscar un contacto por su nombre.

contactos = {}

def agregar_contacto():
    nuevoContacto = str(input("Escribe el nombre del nuevo contacto: "))
    numeroContacto = str(input("Escribe el número del contacto: "))
    contactos[nuevoContacto] = numeroContacto
    print(f"\033[32mContacto agregado\033[0m {nuevoContacto} - {contactos[nuevoContacto]}")
    
def mostrar_contactos():
    for clave,valor in contactos.items():
        print(f"\033[33m{clave}\033[0m : \033[32m{valor}\033[0m")
        
def buscar_contacto():
    nombre_contacto = str(input("Escribe el nombre del usuario que deseas buscar: "))
    if nombre_contacto in contactos:
        print(f"{nombre_contacto} - {contactos[nombre_contacto]}")

while True:
    print("""

          1) Agregar nuevo contacto
          2) Mostrar todos los contactos
          3) Buscar un contacto por su nombre
          4) Salir
          """)
    try:
        opcion = int(input("Elige una opción: "))

        match opcion:
            case 1:

                agregar_contacto()

            case 2:
                
                mostrar_contactos()
            
            case 3:
                buscar_contacto()
                
            case 4:
                print("Salir")
                break

    except:
        print("Elije una opción del 1 al 4")
    