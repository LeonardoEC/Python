valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese otro valor: "))
contador = 0

if valor1 > valor2:
    while valor1 > valor2:

        contador +=1
        valor2 +=1
    print(contador)

elif valor2 > valor1:
    while valor2 > valor1:

        contador +=1
        valor1 +=1

    print("-",contador, sep="")
