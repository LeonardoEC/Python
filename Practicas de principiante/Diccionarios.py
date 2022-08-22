#creacion
datos = {'nomrbe':"Carlos",'apellido':"",'edad':22,'cursos':["Python","Django","Java"]}

#acceso
print(datos["nomrbe"])
print(datos["apellido"])
print(datos["edad"])
print(datos["cursos"])

print("-"*50)

#Acceso a lista
print(datos["cursos"][0])
print(datos["cursos"][1])
print(datos["cursos"][2])

print("-"*50)

#Recorrido
for key in datos:
    print(key,":",datos[key])

print("-"*50)


cambio = dict(nombre='nombre raro')
print(cambio)



