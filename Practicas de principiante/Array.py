#arry
from traceback import print_tb


casa = []

for i in range(3):

    casa.append(input("ingresa los items de la casa: "))

print(casa)

nuevo_mueble = casa.append(input("agrega algo mas a la casa"))

print(casa)

#encunetra la palabra

palabra = "cada uno cada uno cada uno cada uno cada uno"

#encuentra la palabra

print(palabra.find("o"))

#parte
print(palabra[0:3])

#esta en? 
print("a" in palabra)

#test
print(palabra.capitalize)

#print(dir(palabra))
