t = 0

while True:
    
    n = int(input("Ingresa un valor: "))
    if n == 0:
        break

    #Forma 1
    resultado = n + n
    
    #Forma 2
    r = n
    r += n

    #Forma 3
    t += n

print(resultado)
print(r)
print(t)
