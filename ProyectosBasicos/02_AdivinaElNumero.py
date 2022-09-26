from random import random
import random

def adivinaElNumero(x):

    intento = 0

    print("==============================")
    print("   ¡Bienvenido(a) al Juego!"   )
    print("==============================")
    
    numero_aleatorio = random.randint(1,x)

    while True:

        intento +=1

        valor = int(input("Intenta adivinar: "))

        if valor == numero_aleatorio:
            print("Adivinaste¡¡ y lo hiciste en: ",intento," intentos")
            break
        else:
            print("Sigue intenando")


adivinaElNumero(int(input("En que cargo jugaremos? ")))