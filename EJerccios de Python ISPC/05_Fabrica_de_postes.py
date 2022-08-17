madera = int(input("Cuantos postes de madera hay? "))
poste_fabricado = 0

while madera > 0:

    longi = float(input("Que longitud tendra el poste? "))

    if longi == 1.7 or longi == 1.8:
        poste_fabricado += 1

    madera -=1

print("Se crearon" ,poste_fabricado, "postes")
