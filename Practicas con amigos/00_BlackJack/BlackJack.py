import random

As = (11, 1)
J = 10
Q = 10
K = 10
palos = ('Picas', 'Corazones', 'Rombos', 'Tréboles')

carta = (As[0], J, Q, K, 2, 3, 4, 5, 6, 7, 8, 9,)

repartir = totalU = totalC = 0
print('---------------------------------------')
print('          Juego BLackjack              ')
print('--------------------------------------- \n')
while repartir <= 2:
    repartir +=1
    x = random.choice(carta)
    y = random.choice(carta)
    if repartir == 1: 
        print("Mi primer valor es Jugador: ","[",x,"]")
        print("Mi primer valor es Crupier: ","[",y,"]\n")
        totalU = x
        totalC = y
    if repartir == 2:
        print("Segundo valor del Jugador", "[",x,"]")
        print("Segundo valor del Crupier", "[",y,"]\n")
        totalU += x
        totalC += y
    if totalU > 21 and totalC > 21:
        As = 1
    if repartir > 2 and totalU <= 20:
        pregunta = int(input("Otra carta ?\n1_Si\n2_no\nRespuesta: "))
        print("Tercer valor del jugador", "[",x,"]")
        totalU += x
        if totalC <= 16:
            print("Tercer valor del Crupier", "[",y,"]")
            totalC += y
        else:
            print("Crupier llego a 17 o mas")
           
print("valor total de jugador", totalU)
print("valor total de crupier", totalC)
# if suma1 > 21:
   #     As = 1