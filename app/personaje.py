import pygame

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, nivel=1):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.experiencia = 0
        self.inventario = []

    def atacar(self, enemigo):
        # Fórmula básica para calcular daño
        daño = max(0, self.ataque - enemigo.defensa)
        enemigo.recibir_daño(daño)
        print(f"{self.nombre} atacó a {enemigo.tipo} causando {daño} de daño.")

    def defenderse(self, daño):
        daño_recibido = max(0, daño - self.defensa)
        self.vida -= daño_recibido
        print(f"{self.nombre} recibió {daño_recibido} de daño. Vida restante: {self.vida}")

    def recolectar_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"{self.nombre} recolectó {objeto.nombre}.")

    def usar_objeto(self, objeto):
        if objeto in self.inventario:
            objeto.usar(self)
            self.inventario.remove(objeto)

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 10
        self.ataque += 5
        self.defensa += 3
        print(f"{self.nombre} subió al nivel {self.nivel}!")
