import pygame

class Nave():
    """Sirve para gestionar el comportamiento de la nave"""

    def __init__(self,pantalla):
        """Inicializa la nave y establece su posicion de partida"""
        self.pantalla = pantalla

        #Cara la imangen de la nave y obtiene su rect
        #rect = rectangulo
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        #Empieza cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
    
    def blitme(self):
        """Dibuja la nave en su ubicacion actual"""
        self.pantalla.blit(self.imagen,self.rect)