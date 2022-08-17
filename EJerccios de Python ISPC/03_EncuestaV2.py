personas = 0
encuensta = []

while personas < 7:

    repuesta = input("¿Como es la situacion economica del pais?\n1- Mejorando\n2- Regular\n3- Mala\n\nrepuesta: ")

    if repuesta == "1":
        encuensta.append("Mejorando")

    elif repuesta == "2":
        encuensta.append("Regular")
        
    elif repuesta == "3":
        encuensta.append("Mala")
        
    personas +=1

print("\n\nResultados de la encuesta")

print("\nMejorando: ", encuensta.count("Mejorando"))
print("\nRegular: ", encuensta.count("Regular"))
print("\nMala: ", encuensta.count("Mala"))