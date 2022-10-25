class Perro:
    #Constructor predeterminado
    pata = 4
    hamber = 50
 
    #Constructor parametral
    def __init__(self,nombre = "Ramos"):
        self._nombre = nombre

    def comer(self):
        return "Comiendo"

    @property #Getter
    def nombre(self):
        return self._nombre
 
#    @nombre.setter #Setter
#    def nombre(self,nombre):
#        self._nombre = nombre

#cani = Perro("Tomas")
berrin = Perro()
print(berrin.nombre)
#print(cani.pata)
#print(cani.nombre)
#print(cani.comer())
#cani.nombre = "Dario"
#print(cani.nombre)