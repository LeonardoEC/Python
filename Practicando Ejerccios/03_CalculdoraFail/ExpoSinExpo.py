
Base = int(input("Base: "))
Exponente = int(input("Exponente: "))
resultado = 1

while Exponente >= 1:
    Exponente -=1
    resultado *= Base

print(resultado)

