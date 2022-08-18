from email.contentmanager import raw_data_manager
from os import remove
import random
from secrets import choice

salud = 100
inventario = []
items = ["Espada", "Escudo"]
dragon = 300

while True:

    #Quien gana
    if salud <= 0:
        print("Has muerto")
        break
    elif dragon <= 0:
        print("Has derrotado al dragon")
        break

    golpe = random.randint(0,2)
    accion = int(input("preciona: \n1: Si quieres golpear\n2: Si te quieres defender\n"))

    #Combate
    if accion == 1:
        if "Espada" in inventario:
            golpe *= 10
            dragon -= golpe
        else:
            dragon -= golpe

    #Dropeo
    if len(inventario) < 2:
        drop = random.randint(1,2)
        if drop == 1:
            soltado = random.choice(items)
            inventario.append(soltado)
            items.remove(soltado)
            print("Te toco:",soltado)
        else:
            print("No hay mas Items")
    else:
        print("No dropeo nada")

    #AtkDragon
    atkDragon = random.randint(2,10)
    CupHit = random.randint(1,200)
    if CupHit < 100 and CupHit % 2 != 0 and "Escudo" in inventario:
        atkDragon -= 4
        salud -= atkDragon
    else:
        salud -= atkDragon 

    

    print(dragon)
    print(salud)