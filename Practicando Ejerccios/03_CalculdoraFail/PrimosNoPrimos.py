def vprimo(x):

    for i in range(2,x):
        if (x%i) == 0:
            return "No es primo"
    return "Es primo"

print(vprimo(int(input("Ingresa un numero: "))))