valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese otro valor: "))
resultado = []

for i in range(0,valor1):
    resultado.append(i)

for i in range(0,valor2):
    resultado.append(i)

print("El resultado de la suma es:",len(resultado))