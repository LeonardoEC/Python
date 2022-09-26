import random

def AdivinaMiNumero(x):

    print("==============================")
    print("   ¡Bienvenido(a) al Juego!"   )
    print("==============================")

    oportunidad = True

    contador = 0

    while oportunidad:

        inicio = random.randint(0,x)

        if inicio > x or inicio < x:
            print("Falle, elegi: ", inicio)
            
            OtraOportunidad = int(input("Me das otra oportunidad ? 1_Si 2_No "))

            if OtraOportunidad == 1:
                print("Gracias, seguire intentando :D")
            else:
                print("Esta bien, ganaste :C")
                oportunidad = False
        
        elif inicio == x:
            print("Gane¡¡ el numero era: ", inicio, "y me tomo",contador,"intentos")
            oportunidad = False
            

        contador +=1

AdivinaMiNumero(int(input("Con que valor iniciamos?: ")))
