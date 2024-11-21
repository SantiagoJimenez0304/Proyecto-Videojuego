class Enemigo:
    def __init__(self, tipo, vida, ataque, defensa):
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, personaje):
        daño = max(0, self.ataque - personaje.defensa)
        personaje.defenderse(daño)
        print(f"{self.tipo} atacó a {personaje.nombre} causando {daño} de daño.")

    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.tipo} fue derrotado.")
