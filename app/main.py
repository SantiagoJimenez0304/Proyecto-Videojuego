from personaje import Personaje
from enemigo import Enemigo
from objeto import Objeto, TrampaExplosiva, Tesoro, Arma
from mapa import Mapa
from combate import Combate
from juego import Juego
import pygame
def correr(self):
    print("Inicializando el juego...")
    self.inicializar()  # Asegúrate de que esto no tenga errores
    ejecutando = True

    while ejecutando:
        print("Iteración del bucle principal...")
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                print("Cerrando el juego...")
                ejecutando = False

        self.actualizar()
        self.dibujar()
        self.clock.tick(60)

    pygame.quit()
    print("Juego finalizado.")

if __name__ == "__main__":
    juego = Juego()
    juego.correr()
