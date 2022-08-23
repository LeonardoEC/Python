notas = []

while True:
    profesor = int(input("Ingrese las notas: "))
    notas.append(profesor)
    if len(notas) >= 3:
        break

print(round(sum(notas)/len(notas)))