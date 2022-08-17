from itertools import count

personas = 0
repuestas = []

while personas < 7:
    
    pregunta = input("¿Como es la situacion economica del pais? ")

    repuestas.append(pregunta)

    r = repuestas.count("Mejorando")
    q = repuestas.count("Regular")
    t = repuestas.count("Mala")

    personas += 1

print("Mejorando",r)
print("Regular", q)
print("Mala",t)
