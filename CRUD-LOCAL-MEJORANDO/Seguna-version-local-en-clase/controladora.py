import os
import humano

def mostrar_opciones():
    print('CRUD EJEMPLO')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]reate')
    print('[R]ead - Leer')
    print('[U]pdate - Actualizar')
    print('[D]elete  - Elimnar')
    print('[S]ALIR')

lista_de_humanos = []

def run():

    mostrar_opciones()

    command = input()
    command = command.upper()

    while True:
        if command == 'C':
            print("CREACION DE USUARIO")
            print('*' * 50)

            dni = input("ingrese un dni: ")
            nombre = input("ingres su nombre: ")
            apellido = input("ingrese su apellido: ")

            lista_de_humanos.append(humano.Humano(dni, nombre, apellido))

            print("Humano creado")

            command = ""

        elif command == 'R':
            print("IMPRIMIENDO TODOS LOS Humanos")
            print('*' * 50)

            for i in lista_de_humanos:
                print(i.dni, i.nombre, i.apellido)

            command = ""

        elif command == 'U':

            humano1 = humano.Humano("1", "Tomas", "Ramos")

            print("ACTUALIZACION")
            print('*' * 50)

            idBuscador = input("Ingrese el DNI: ")

            if idBuscador == humano1.dni:
                humano1.nombre = input("ingresa un nuevo nombre: ")
                humano1.apellido = input("ingresa un nuevo apellido: ")

                command = ""

                print(humano1.nombre, humano1.apellido)


        elif command == 'D':
            humano1 = humano.Humano("1", "Tomas", "Ramos")
            idBuscador = input("Ingrese el Id: ")

            if idBuscador == humano1.dni:
                del humano1

                command = ""

                print("Humano fue eliminado")

        elif command == 'S':
            os._exit(1)

        else:
            run()

if __name__ == "__main__":
    run()