from calendar import c


class Auto:

    def __init__(self) -> None:
        self.ruedas = 4

    def acomplado(self):
        return self.ruedas + 4

    def __add__(self,other):
        return Auto(self.ruedas + other.ruedas)

class Acomplado:

    def __init__(self) -> None:
        self.ruedas = 6
    
    def __add__(self, other):
        return Acomplado(self.ruedas + other.ruedas)


chata = Auto()
aco = Acomplado()

print(chata.ruedas)
print(chata.acomplado())

print(aco.ruedas)
print(aco + chata)