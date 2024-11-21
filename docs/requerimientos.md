# Taller Videojuego

## Listado de Requerimientos Funcionales

### 1. Creación de Personajes
- El sistema debe permitir la creación de un personaje con los siguientes atributos:
  - *Puntos de vida*: Representa la resistencia del personaje al daño.
  - *Ataque*: Define el poder de ataque del personaje.
  - *Defensa*: Representa la capacidad del personaje para resistir el daño enemigo.
  - *Nivel*: Indica el progreso del personaje y habilita nuevas habilidades.
  - *Inventario*: Almacena los objetos que el personaje recolecta.

### 2. Creación de Enemigos
- El sistema debe permitir la creación de enemigos con los siguientes atributos:
  - *Puntos de vida*: Representa la resistencia del enemigo al daño.
  - *Ataque*: Define el poder de ataque del enemigo.
  - *Defensa*: Representa la capacidad del enemigo para resistir el daño del personaje.
  - *Tipo*: Puede variar según el comportamiento o habilidades del enemigo (ej: volador, terrestre, etc.).

### 3. Creación de Objetos
- El sistema debe permitir la creación de los siguientes tipos de objetos:
  - *Trampas explosivas*: Deben tener diferentes alcances y efectos negativos sobre el personaje.
  - *Tesoros*: Deben tener diferentes valores que se traduzcan en dinero para el personaje al venderlos.
  - *Armamento/Defensa*: El personaje debe poder comprar y vender armamento para mejorar su ataque y defensa.

### 4. Funcionalidades del Personaje
- El sistema debe permitir al personaje:
  - Atacar y defenderse de los enemigos.
  - Recolectar objetos (como trampas y tesoros).
  - Adquirir, usar o vender armas y defensas.
  - Interactuar con el entorno (recolectar objetos, esquivar obstáculos).

### 5. Creación de Escenarios
- El sistema debe permitir la creación de un mapa del juego que incluya:
  - Un *planeta desconocido* con diferentes áreas para explorar.
  - *Ubicación aleatoria* de enemigos y objetos.
  - *Zonas de venta* para comprar armamento.

### 6. Sistema de Combate
- El sistema debe implementar un sistema de combate que incluya:
  - Ataque y defensa por parte del personaje y los enemigos.
  - Cálculo de daño en base a los atributos de ataque, defensa y puntos de vida.
  - Efectos especiales según el tipo de ataque y la interacción entre objetos (ej: explosión de una trampa).

### 7. Progresión del Personaje
- El sistema debe permitir la progresión del personaje mediante:
  - *Aumento de nivel* al obtener experiencia (derrotando enemigos, recolectando objetos valiosos).
  - *Mejora de atributos* (puntos de vida, ataque, defensa) al subir de nivel.
  - *Acceso a nuevo armamento y defensas* a medida que avanza el nivel del personaje.

### 8. Condiciones de Victoria
- El sistema debe definir las condiciones de victoria:
  - Completar la exploración del mapa del juego.
  - Derrotar a un jefe final.
  - Alcanzar un puntaje determinado.