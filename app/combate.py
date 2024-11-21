class Combate:
    @staticmethod
    def iniciar(personaje, enemigo):
        print(f"¡Comienza el combate entre {personaje.nombre} y {enemigo.tipo}!")

        while personaje.vida > 0 and enemigo.vida > 0:
            # Turno del personaje
            personaje.atacar(enemigo)
            if enemigo.vida <= 0:
                print(f"{enemigo.tipo} fue derrotado. ¡Victoria!")
                return True  # Combate ganado

            # Turno del enemigo
            enemigo.atacar(personaje)
            if personaje.vida <= 0:
                print(f"{personaje.nombre} fue derrotado. ¡Derrota!")
                return False  # Combate perdido
