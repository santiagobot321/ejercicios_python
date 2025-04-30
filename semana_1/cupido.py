print("Alma gemela")

print("Por favor responde con Si/No/Tal vez")

contador = 0

lista = [
        
        input("¿Crees en el amor para toda la vida? "),
        input("¿Te gustan las relaciones estables a largo plazo (casa, proyectos, viajes)? "),
        input("¿Te sientes cómoda hablando de tus emociones? "),
        input("¿Crees que la fidelidad es escencial en una relación? "),
        input("¿Te gusta pasar tiempo a solas sin que eso afecte tu relación? "),
        input("¿Te gustaría tener una pareja que te acompañe en tu crecimiento personal? "),
        input("¿Has trabajado en sanar heridas emocionales del pasado? "),
        input("¿Estás abierta al compromiso real? "),
        input("¿Te gustaría que tu pareja también sea tu mejor amigo? "),
        input("¿Guardas secretos que pueden lastimar en un futuro? ") 
         
         ]

for respuesta in range(len(lista)):
    
    if lista[respuesta].lower() == "si":
        contador += 10
    elif lista[respuesta].lower() == "tal vez":
        contador += 5    
    else:
        contador -= 3
              
if 85 < contador <= 100:
    print("Alma gemela")
elif 65 < contador <= 84:
    print("Muy buena compatibilidad")
elif 45 < contador <= 64:
    print("Compatibilidad media")
elif 25 < contador <= 44:
    print("Compatibilidad baja")
else:
    print("Muy poca compatilibidad")        

print(contador)