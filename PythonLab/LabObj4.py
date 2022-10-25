class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        print(self.__nombre)
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @nombre.getter
    def nombre(self):
        return self.__nombre

B = Perro("Tomas",22)

print(B.nombre)
B.nombre = "Angusto"
print(B.nombre)
