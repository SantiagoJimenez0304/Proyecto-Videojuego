import pygame
import random
from personaje import Personaje
from mapa import Mapa
import os

class Juego:
    def __init__(self):
        pygame.init()

        # Dimensiones de la ventana
        self.ancho = 800
        self.alto = 600

        # Configuración de la pantalla
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Aventura en el Planeta Desconocido")

        # Reloj para controlar FPS
        self.clock = pygame.time.Clock()

        # Variables del juego
        self.personaje = None
        self.mapa = None
        self.juego_terminado = False
        self.tiempo_inicio = pygame.time.get_ticks()
        self.ultimo_incremento_velocidad = pygame.time.get_ticks()  # Marca inicial de tiempo para control de velocidad
        self.enemigos = []
        self.velocidad_base_enemigo = 2
        self.max_enemigos = 3
        self.monedas_recolectadas = 0
        self.nivel = 1  # Nivel inicial
        self.meta_monedas = 10  # Meta inicial
        self.cargar_musica()

        # Cargar imágenes
        self.fondo = pygame.image.load("assets/fondo.png")
        self.personaje_imagen = pygame.transform.scale(
            pygame.image.load("assets/personaje.png"), (50, 50))
        self.enemigo_imagen = pygame.transform.scale(
            pygame.image.load("assets/enemigo.png"), (50, 50))
        self.objeto_imagen = pygame.transform.scale(
            pygame.image.load("assets/objeto.png"), (35, 35))

        # Posiciones iniciales
        self.personaje_pos = [400, 300]
        self.objeto_pos = self.generar_posicion_aleatoria()
    
    def generar_posicion_aleatoria(self):
        """Genera una posición aleatoria dentro de los límites de la pantalla."""
        return [
            random.randint(0, self.ancho - 35),  # Limita en el ancho menos el tamaño del objeto
            random.randint(0, self.alto - 35)   # Limita en el alto menos el tamaño del objeto
        ]

    def cargar_musica(self):
        """Carga y reproduce música de fondo."""
        pygame.mixer.init()
        pygame.mixer.music.load("assets/musica_fondo.mp3")  # Ruta al archivo de música
        pygame.mixer.music.set_volume(0.2)  # Ajusta el volumen (0.0 a 1.0)
        pygame.mixer.music.play(-1)  # Reproduce en bucle (-1 para infinito)

    def inicializar(self):
        """Inicializa los elementos principales del juego."""
        # Crear personaje y mapa
        self.personaje = Personaje("Héroe", 100, 20, 10)
        self.mapa = Mapa(self.ancho, self.alto)
        self.mapa.generar_aleatorio()

        # Generar enemigos iniciales
        self.enemigos = []  # Reinicia la lista de enemigos
        for _ in range(2):  # Genera dos enemigos al inicio
            self.generar_enemigo()

        self.juego_terminado = False
        self.tiempo_inicio = pygame.time.get_ticks()  # Reinicia el tiempo del juego
        self.monedas_recolectadas = 0  # Reinicia el contador de monedas
        print("Juego inicializado.")

    def generar_enemigo(self):
        """Genera un nuevo enemigo en una posición aleatoria si no excede el máximo."""
        if len(self.enemigos) < self.max_enemigos:
            x = random.randint(0, self.ancho - 50)
            y = random.randint(0, self.alto - 50)
            velocidad_x = random.choice([-self.velocidad_base_enemigo, self.velocidad_base_enemigo])
            velocidad_y = random.choice([-self.velocidad_base_enemigo, self.velocidad_base_enemigo])
            self.enemigos.append({"pos": [x, y], "vel": [velocidad_x, velocidad_y]})

    def correr(self):
        """Bucle principal del juego."""
        self.mostrar_menu()
        self.inicializar()
        ejecutando = True

        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False

                if self.juego_terminado and evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:  # Salir al presionar ESC
                        ejecutando = False

            if not self.juego_terminado:
                # Mover personaje basado en teclas presionadas
                self.mover_personaje()

                # Actualizar el estado del juego
                self.actualizar()

                # Incrementar velocidad de los enemigos cada 5 segundos
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - self.ultimo_incremento_velocidad >= 5000:  # 5 segundos
                    self.incrementar_velocidad_enemigos()
                    self.ultimo_incremento_velocidad = tiempo_actual

                # Generar enemigos adicionales si hay menos del máximo
                if len(self.enemigos) < self.max_enemigos:
                    self.generar_enemigo()

            # Dibujar elementos en pantalla
            self.dibujar()

            # Controlar los FPS
            self.clock.tick(60)

        pygame.quit()

    def mover_personaje(self):
        """Gestiona el movimiento del personaje con límites."""
        keys = pygame.key.get_pressed()
        velocidad = 5
        if keys[pygame.K_UP] and self.personaje_pos[1] > 0:
            self.personaje_pos[1] -= velocidad
        if keys[pygame.K_DOWN] and self.personaje_pos[1] < self.alto - 50:
            self.personaje_pos[1] += velocidad
        if keys[pygame.K_LEFT] and self.personaje_pos[0] > 0:
            self.personaje_pos[0] -= velocidad
        if keys[pygame.K_RIGHT] and self.personaje_pos[0] < self.ancho - 50:
            self.personaje_pos[0] += velocidad

    def incrementar_velocidad_enemigos(self):
        """Incrementa la velocidad base de los enemigos."""
        self.velocidad_base_enemigo += 0.5  # Incrementa la velocidad base
        for enemigo in self.enemigos:
            enemigo["vel"][0] += 0.5 if enemigo["vel"][0] > 0 else -0.5
            enemigo["vel"][1] += 0.5 if enemigo["vel"][1] > 0 else -0.5
        print("Velocidad de enemigos incrementada a:", self.velocidad_base_enemigo)


    def mostrar_menu(self):
        """Muestra el menú principal."""
        menu_activo = True
        fuente_titulo = pygame.font.SysFont("Arial", 48)
        fuente_opciones = pygame.font.SysFont("Arial", 36)

        while menu_activo:
            self.pantalla.fill((0, 0, 0))  # Fondo negro

            # Título
            titulo = fuente_titulo.render("Aventura en el Planeta Desconocido", True, (255, 255, 255))
            self.pantalla.blit(titulo, (self.ancho // 2 - titulo.get_width() // 2, 100))

            # Opciones
            jugar_opcion = fuente_opciones.render("1. Jugar", True, (255, 255, 255))
            reglas_opcion = fuente_opciones.render("2. Reglas", True, (255, 255, 255))
            salir_opcion = fuente_opciones.render("3. Salir", True, (255, 255, 255))

            self.pantalla.blit(jugar_opcion, (self.ancho // 2 - jugar_opcion.get_width() // 2, 250))
            self.pantalla.blit(reglas_opcion, (self.ancho // 2 - reglas_opcion.get_width() // 2, 300))
            self.pantalla.blit(salir_opcion, (self.ancho // 2 - salir_opcion.get_width() // 2, 350))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:  # Jugar
                        menu_activo = False
                    elif evento.key == pygame.K_2:  # Reglas
                        self.mostrar_reglas()
                    elif evento.key == pygame.K_3:  # Salir
                        pygame.quit()
                        exit()
    def mostrar_reglas(self):
        """Muestra las reglas del juego."""
        reglas_activo = True
        fuente_reglas = pygame.font.SysFont("Arial", 36)
        fuente_pequena = pygame.font.SysFont("Arial", 24)

        while reglas_activo:
            self.pantalla.fill((0, 0, 0))  # Fondo negro

            # Título
            titulo = fuente_reglas.render("Reglas del Juego", True, (255, 255, 255))
            self.pantalla.blit(titulo, (self.ancho // 2 - titulo.get_width() // 2, 100))

            # Reglas
            regla_1 = fuente_pequena.render("1. Intenta no chocar con los enemigos.", True, (255, 255, 255))
            regla_2 = fuente_pequena.render("2. Cada 5 segundos, los enemigos aumentarán su velocidad.", True, (255, 255, 255))

            self.pantalla.blit(regla_1, (self.ancho // 2 - regla_1.get_width() // 2, 200))
            self.pantalla.blit(regla_2, (self.ancho // 2 - regla_2.get_width() // 2, 250))

            # Instrucción para volver
            regresar = fuente_pequena.render("Presiona ESC para regresar al menú principal.", True, (255, 255, 0))
            self.pantalla.blit(regresar, (self.ancho // 2 - regresar.get_width() // 2, 400))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:  # Volver al menú
                        reglas_activo = False

    def actualizar(self):
        """Lógica de actualización del juego."""
        # Movimiento de enemigos
        for enemigo in self.enemigos:
            enemigo["pos"][0] += enemigo["vel"][0]
            enemigo["pos"][1] += enemigo["vel"][1]
            if enemigo["pos"][0] > self.ancho - 50 or enemigo["pos"][0] < 0:
                enemigo["vel"][0] *= -1
            if enemigo["pos"][1] > self.alto - 50 or enemigo["pos"][1] < 0:
                enemigo["vel"][1] *= -1

        # Colisión con monedas
        personaje_rect = pygame.Rect(self.personaje_pos[0], self.personaje_pos[1], 50, 50)
        objeto_rect = pygame.Rect(self.objeto_pos[0], self.objeto_pos[1], 35, 35)

        if personaje_rect.colliderect(objeto_rect):  # Detecta colisión con la moneda
            self.monedas_recolectadas += 1
            self.objeto_pos = self.generar_posicion_aleatoria()  # Genera una nueva moneda

        # Colisión con enemigos
        for enemigo in self.enemigos:
            enemigo_rect = pygame.Rect(enemigo["pos"][0], enemigo["pos"][1], 50, 50)
            if personaje_rect.colliderect(enemigo_rect):  # Detecta colisión con un enemigo
                print("¡Colisión con el enemigo! Has perdido.")
                self.juego_terminado = True
                break

        # Verificar si se completa el nivel
        if self.monedas_recolectadas >= self.meta_monedas:
            self.nivel += 1
            if self.nivel == 2:
                self.meta_monedas = 20  # Meta del Nivel 2
                self.velocidad_base_enemigo += 1
                self.max_enemigos += 2
            elif self.nivel == 3:
                self.meta_monedas = 50  # Meta del Nivel 3
                self.velocidad_base_enemigo += 2
                self.max_enemigos += 3
            elif self.nivel > 3:
                print("¡Has completado todos los niveles!")
                self.juego_terminado = True

            self.monedas_recolectadas = 0  # Reinicia el contador
            print(f"¡Nivel {self.nivel} alcanzado!")

    def dibujar(self):
        """Dibuja todos los elementos del juego en la pantalla."""
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.personaje_imagen, self.personaje_pos)

        for enemigo in self.enemigos:
            self.pantalla.blit(self.enemigo_imagen, enemigo["pos"])

        # Dibujar moneda
        self.pantalla.blit(self.objeto_imagen, self.objeto_pos)

        # Mostrar tiempo de supervivencia
        tiempo_transcurrido = (pygame.time.get_ticks() - self.tiempo_inicio) // 1000
        fuente = pygame.font.SysFont("Arial", 24)
        texto_tiempo = fuente.render(f"Tiempo: {tiempo_transcurrido}s", True, (255, 255, 255))
        self.pantalla.blit(texto_tiempo, (10, 10))

        # Mostrar monedas recolectadas
        texto_monedas = fuente.render(f"Monedas: {self.monedas_recolectadas}/{self.meta_monedas}", True, (255, 255, 0))
        self.pantalla.blit(texto_monedas, (10, 40))

        # Mostrar nivel
        texto_nivel = fuente.render(f"Nivel: {self.nivel}", True, (255, 255, 255))
        self.pantalla.blit(texto_nivel, (10, 70))

        if self.juego_terminado:
            texto = fuente.render("¡Juego completado! Presiona ESC para salir.", True, (255, 0, 0))
            self.pantalla.blit(texto, (self.ancho // 2 - texto.get_width() // 2, self.alto // 2))

        pygame.display.flip()


