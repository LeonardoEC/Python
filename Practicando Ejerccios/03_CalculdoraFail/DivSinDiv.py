Dividendo = int(input("Dividendo: "))
Divisor = int(input("Divisor: "))
resultado = 0
cociente = 0

while True:
    cociente+=1
    resultado+= Divisor

    if resultado == Dividendo or resultado > Dividendo:
        break

print("El cociente es:",cociente)
print("El resto es:", resultado - Dividendo)

