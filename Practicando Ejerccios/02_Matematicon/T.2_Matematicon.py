import random

while True:

    x = random.randint(1,10)
    y = random.randint(1,10)
    s = random.randint(0,3)

    simbolo = ["+","-","*","/"]

    Eleccion = simbolo[s]

    print("Cual es el valor de ",x, Eleccion ,y)
    r = int(input("Preciona '00' para salir o dime tu respuesta: "))

    if r == 00:
        break

    elif Eleccion == "+":
        if r == x+y:
            print("Correcto, el resultado es: ",r)
        else:
            print("Incorrecto, la respuesta era: ",x+y)
    elif Eleccion == "-":
        if r == x-y:
            print("Correcto, el resultado es: ",r)
        else:
            print("Incorrecto, la respuesta era: ",x-y)
    elif Eleccion == "*":
        if r == x*y:
            print("Correcto, el resultado es: ",r)
        else:
            print("Incorrecto, la respuesta era: ",x*y)
    elif Eleccion == "/":
        if r == x//y:
            print("Correcto, el resultado es: ",r)
        else:
            print("Incorrecto, la respuesta era: ",x//y)
    