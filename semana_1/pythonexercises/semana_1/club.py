edad = int(input("¿Cuál es tu edad?: "))
pase = input("¿Tienes pase dorado?: ").lower()

if edad >= 18:
    if edad > 18 and pase == "no":
        print("no puedes pasar")
    
    elif edad == 18 and pase == "si" or "no":
        print("Pasa")
else:
    print("No puedes pasar")
