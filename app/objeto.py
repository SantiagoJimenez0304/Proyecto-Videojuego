class Objeto:
    def __init__(self, nombre):
        self.nombre = nombre


class TrampaExplosiva(Objeto):
    def __init__(self, nombre, daño):
        super().__init__(nombre)
        self.daño = daño

    def detonar(self, personaje):
        personaje.defenderse(self.daño)
        print(f"¡Trampa {self.nombre} detonada! {personaje.nombre} recibió {self.daño} de daño.")


class Tesoro(Objeto):
    def __init__(self, nombre, valor):
        super().__init__(nombre)
        self.valor = valor

    def vender(self):
        print(f"El tesoro {self.nombre} fue vendido por {self.valor} monedas.")
        return self.valor


class Arma(Objeto):
    def __init__(self, nombre, mejora_ataque):
        super().__init__(nombre)
        self.mejora_ataque = mejora_ataque

    def usar(self, personaje):
        personaje.ataque += self.mejora_ataque
        print(f"{personaje.nombre} equipó {self.nombre}, aumentando su ataque en {self.mejora_ataque}.")
