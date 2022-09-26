import sys

import pygame

from configuraciones import Configuraciones

from nave import Nave

def run_game():
    
    # Inicializar el juego, las configuraciones y crear un objeto patalla
    pygame.init()

    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    #pantalla = pygame.display.set_mode((800,600)) --> codigo viejo
    pygame.display.set_caption("Invasion alienigena")

    # Crea una nave
    nave = Nave(pantalla)

    # Establece el color de fondo
    #bg_color = (230,230,230)

    # Iniciar el bucle principal del juego
    while True:
        
        # Escuchar eventos de teclado o de raton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        # Volver a dibujar la pantalla durante cada pasada por el bucle
        pantalla.fill(ai_configuraciones.bg_color)
        #pantalla.fill(bg_color) --> codigo viejo
        nave.blitme()

        # Hacer visible la pantalla dibujada mas reciente
        pygame.display.flip()


run_game()


    
