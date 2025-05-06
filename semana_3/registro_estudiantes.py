estudiantes = {}

def agregar_estudiante():
    
    nombre_estudiante = str(input("Escribe el nombre del estudiante: "))
    edad_estudiante = int(input("Escribe la edad del estudiante: "))
    calificacion = float(input("Escribe la nota del estudiante: "))
    estudiantes[nombre_estudiante] = {"edad":edad_estudiante,"calificacion":calificacion}
    print(f"{nombre_estudiante} - {estudiantes[nombre_estudiante]}")

def modificar_calificacion():
    
    nombre_estudiante = str(input("Ingresa el nombre del alumno para modificar su nota: "))
    if nombre_estudiante in estudiantes:
        calificacion = float(input("Ingresa la nueva calificación: "))
        estudiantes[nombre_estudiante]["calificacion"] = calificacion
        print(f"{nombre_estudiante} - {estudiantes[nombre_estudiante]}")
        
def mostrar_info():
    for clave,valor in estudiantes.items():
        print(f"{clave} : {valor}")
        
        
def eliminar_alumno():
    nombre_estudiante = str(input("Ingresa el nombre del usuario que desea eliminar: "))
    if nombre_estudiante in estudiantes:
        del estudiantes[nombre_estudiante]
        print(f"\033[32m{nombre_estudiante} ha sido eliminado correctamente\033[0m")
        
while True:
    print("""
          
          1) Agregar nuevo estudiante
          2) Modificar calificación
          3) Mostrar la información de todos los estudiantes
          4) Eliminar un estudiante por su nombre
          5) Salir
          
          """)
    
    
    try:
        
        opcion = int(input("Ingresa una opción: "))
        
        match opcion:
            case 1:
                
                agregar_estudiante()

            case 2:
                
                modificar_calificacion()
                
            case 3:
                
                mostrar_info()
                
            case 4:
                
                eliminar_alumno()
                
            case 5:
                
                print("\033[31m Saliendo... \033[0m")
                break
        
    except ValueError:
        print("""
              \033[31mElige un número del 1 al 5\033[0m
              """)