import persona
import os

def mostrar_opciones():
    print('CRUD EJEMPLO')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]reate')
    print('[R]ead - Leer')
    print('[U]pdate - Actualizar')
    print('[D]elete  - Elimnar')
    print('[S]ALIR')

lista_de_personas = []

def run():

    mostrar_opciones()

    command = input()
    command = command.upper()

    while True:
        if command == 'C':
            print("CREACION DE USUARIO")
            print('*' * 50)

            id = input("ingrese un id: ")
            nombre = input("ingres su nombre: ")
            apellido = input("ingrese su apellido: ")

            lista_de_personas.append(persona.Persona(id, nombre, apellido))

            print(lista_de_personas[0])

            command = ""

        elif command == 'R':
            print("IMPRIMIENDO TODOS LOS CLIENTES")
            print('*' * 50)

            for i in lista_de_personas:
                print(i.id, i.nombre, i.apellido)

            command = ""

        elif command == 'U':
            print("ACTUALIZACION")
            print('*' * 50)

            idBuscador = input("Ingrese un Id: ")

            for i in lista_de_personas:

                if i.id == idBuscador:
                    i.nombre = input("Ingrese el nuevo nombre: ")
                    i.apellido = input("Ingrese el nuevo apellido: ")

                command = ""

        elif command == 'D':
            print("Eliminar")
            print('*' * 50)
            idBuscador = input("Ingrese el Id: ")

            for i in lista_de_personas:

                if idBuscador == i.id:
                    i.id = ""
                    i.nombre = ""
                    i.apellido = ""

                    command = ""
                    print("Persona eliminada")


        elif command == 'S':
            os._exit(1)

        else:
            run()

if __name__ == "__main__":
    run()











