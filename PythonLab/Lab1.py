# var = input("Dame tu variable")

# val = input("Dame el valor de la variable")

# bad_dict = {
#     var: val
# }

# print(bad_dict)

# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))

#print(int("c"))

# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#     return wrap

# def print_text():
#     print("Hello world!")

# print_text = decor(print_text)
# print_text()

#Creando una clase vacia
#class Perro:
    #pass

# class Perro:
#     # El metodo __int__ es llamado al crear el objeto
#     def __init__(self, nombre,raza):
#         print(f"Creado perro {nombre}, {raza}")
        
#         self.nombre = nombre
#         self.raza = raza

# #Creamos un objeto de la clase perro
# mi_perro = Perro("Pancho","Dogo")

# print(mi_perro)

# #mi_perro = Perro("Toby","Bulldog")
# print(type(mi_perro))

# print(mi_perro.nombre)
# print(mi_perro.raza)

class Ejemplo():

    #Metodo creado para ejemplificar una funcion "publica"
    def publico(self):
        return "Soy un método público a la vista de todo"

    #Metodo creado para ejemplificar una funcion "privada"
    def __privado(self):
        return "Soy un método privado a la vista de todo"

objeto = Ejemplo()

print(objeto.publico())
print(objeto.__privado())