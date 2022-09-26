import random

def PiedraPapelTijeras(eleccion):

    print("==============================")
    print("   !Piedra, Papel o Tijeras!"  )
    print("==============================")


    opciones = ["piedra","papel","tijera"]

    
    #Inicio
    while True:
        
        oponente = random.choice(opciones)

        print("Piedra.... Papel.... o Tijera....")
        print(eleccion)
        print(oponente)

        #Si es piedra
        if eleccion == "piedra" and oponente == "tijera":
            return "Ganaste!!"
        elif eleccion == "piedra" and oponente == "papel":
            return "Perdiste!!"
        
        #Si es papel
        elif eleccion == "papel" and oponente == "piedra":
            return "Ganaste!!"
        elif eleccion == "papel" and oponente == "tijera":
            return "Perdiste!!"

        #Si es tijera
        elif eleccion == "tijera" and oponente == "papel":
            return "Ganaste!!"
        elif eleccion == "tijera" and oponente == "piedra":
            return "Perdiste!!"

        #Empate
        if oponente == eleccion:
            print("Empate!!")
        
        eleccion = input("Otra eleccion: ")


print(PiedraPapelTijeras(input("Piedra, papel o tijeras? ")))


