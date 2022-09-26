import random

def Ahorcado():

    #intentos disponibles
    salud = 5

    #Seleccionador de palabra
    words = random.choice([
        "s-o-p-a",
        "c-a-m-e-l-l-o",
        "o-r-e-j-a",
        "p-a-t-o"
        ])
    words = words.upper()
    
    #Restricciones numericas
    Resticnumbe = ["1","2","3","4","5","6","7","8","9","0"]

    """Falta agregar restriccion de caracteres especiales"""

    #Pulido de palabra seleccionada para la condicion de victoria
    condicion = words.replace("-","")

    #Colector de letras bien respondidas
    respuesta = []
    errores = []

    #Convertidor de String a lista -> seprado las letras usando los - para formar la palabra
    words = words.split("-")

    #Cantidad de caracteres que posse la repuesta correcta -> Sirve para organizar las letras por posicion y ocultar la respuesta
    for i in words:
        i = "-"
        respuesta.append(i)

    print("==============================")
    print("   !Bienvenido al Ahorcado!"  )
    print("==============================")

    print("   Te toco una palabra de:",len(words),"letras")
    print("                y")
    print("      Tienes",salud,"intentos")
    print("Palabra: ",respuesta)

    while True:
        
        #Toma de valores
        jugador = input("ingresa una letra: ").upper()

        #Control de errores
        if len(jugador) >= 2 or len(jugador) == 0 or jugador in Resticnumbe:
            print("Cantidad de caracteres o valor incorrectos, intente de nuevo")
            jugador = input("Introduce un caracter: ")
            if len(jugador) >= 2 or len(jugador) == 0 or jugador in Resticnumbe:
                print("Error, cerrando el juego")
                break

        #Contador de vidas
        if jugador not in words:
            print(jugador, "No esta en la palabra")
            errores.append(jugador)
            salud -=1
            if salud != 0:
                print("Fallaste, te quedan:",salud,"intentos")

        #Asignador de letras correctas en repuestas
        if jugador in words:
            print("Correcto¡¡")
            respuesta[words.index(jugador)] = jugador
            words[words.index(jugador)] = "-"
            errores.append(jugador)

        #Condicion de victoria
        if "".join(respuesta) == condicion:
            print("Ganaste, la palabra era","".join(respuesta))
            break


        #Condicion de derrota
        if salud == 0:
            print("perdiste la palabra era:", "".join(condicion))
            break
        
        #Muestra el orden de las letras acertadas en cada pocision
        print("Palabra: ",respuesta)

        #Letras usadas
        print("Estas letras fueron usadas:", errores)

Ahorcado()



