from itertools import count

ingreso = []

while True:
    print("preciona '0' para cerrar el programa")
    n = int(input("Ingresa un valor: "))

    if n == 0:
        break

    ingreso.append(n)

    och = ingreso.count(8)
    onc = ingreso.count(11)
    disti = len(ingreso) - (och + onc)


print("El 8 aparace: ", och , " veces")
print("El 11 aparace: ", onc , " veces")
print("Hay ", disti , " numeros distintos")
