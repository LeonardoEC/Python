Historial2 = (23500, 5960, 2300, 10200, 8900)

total = sum(Historial2)

def Gastosuperior(gasto):

    for i in gasto:

        if i > 5000:
            print(i)

    print("El gasto total de Frida fue: $",total, sep="")

Gastosuperior(Historial2)

