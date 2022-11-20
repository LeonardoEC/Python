class Humano:

    def __init__(self, dni, nombre, apellido):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido

    #getters
    @property
    def dni(self):
        return self._dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    #setter
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

