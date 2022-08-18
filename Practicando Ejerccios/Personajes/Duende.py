#Duende
Salud = 100
Hits = []
pociones = 2

while Salud >= 0:
    print("pociones: ",pociones)

    golpeo = int(input("Preciona 1 para golpear al duende "))

    if golpeo == 1:
        Salud -= 15
    
    if Salud <= 25 and pociones >= 1:
        print("Duende toma pocion")
        Salud = 100
        pociones -= 1
    
    Hits.append(golpeo)

    print("La salud del duende es:",Salud)

print("Fue golpeado", len(Hits))
