#Input Mutante

#1.Input Mutante-Listado - FAil -> No puede ser una lista

# datos = ["Nombre","Apellido","Direccion"]

# for i in datos:
#     repuesta = input(f"Ingresa el siguiente dato",datos[i],":")

#     print("Tu",datos[i],"es:",repuesta)

#2.Input Mutante de una sola linea - FAil - No puedo colocar una coma

# palabra = "nombre"

# pregunta = input("Dime tu",palabra)

#3.Input Mutante - Vabriable listada -> Funciono

# datos = ["Nombre","Apellido","Direccion"]

# for i in datos:
#     almacenador = "Dime tu ",i.lower(),":"
#     convertidor = "".join(almacenador)

#     pregunta = input(convertidor)

#     print(pregunta)

#4.Input Mutante - Subimos el nivel -> Funciona

"""Documentacion: vamos a crear una funcion que tome varios input y los almacene en distintas variables
    18/8/2022: Llegamos a buen puerto podemos solicitar varios input, ahora solo falta hacer que cree variables para ello utilizaremos diccionarios
                """

def MInput(veces:int,tipo,dato):

    for i in range(0,veces):

        almacenar = dato
        convertidor = "".join(almacenar)

        pregunta = tipo(input(convertidor))

        print("pregunta",i,pregunta)


print(MInput(3,str,"Como te llamas"))