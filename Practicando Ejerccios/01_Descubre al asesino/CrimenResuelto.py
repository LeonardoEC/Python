from secrets import choice

#Protagonistas
peronas = ["Ramon","Jose","Antonela","Zaria","Chatran","Manuel","Samantha"]
print("Estas personas estan en la esena del crimen ", peronas)
asesino = choice(peronas)
peronas.remove(asesino)
victimas = peronas

#Esenario
while len(victimas) > 0:
    asesinado = choice(victimas)
    print("asesinarion a:",asesinado)
    victimas.remove(asesinado)

    #Descubre al asesino
    repuesta = input("Quien es el asesino ? ")
    if repuesta == asesino:
        print("Fecilidades lo descubriste, el asesino era", asesino)
        break
    elif len(victimas) == 0:
        print("Fuiste asesinado por",asesino)

print("Sobrevivieron", len(victimas))