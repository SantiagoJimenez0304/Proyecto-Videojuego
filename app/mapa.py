class Mapa:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.areas = []
        self.enemigos = []
        self.objetos = []

    def generar_aleatorio(self):
        print("Mapa generado con enemigos y objetos en ubicaciones aleatorias.")
