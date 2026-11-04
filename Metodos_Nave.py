class NaveEspacial:
    def __init__(self, nombre: str, piloto: str, nivel_escudo: int):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo

    def recibir_disparo(self, daño: int) -> None:
        self.nivel_escudo -= daño
        if self.nivel_escudo <= 0:
            self.nivel_escudo = 0
            print("La nave ha sido destruida")
        else:
            print(f"El escudo restante es de {self.nivel_escudo}")

    def recargar_escudo(self, cantidad: int) -> None:
        if cantidad > 0:
            self.nivel_escudo += cantidad
            print(f"El nuevo nivel del escudo es de {self.nivel_escudo}")


nave = NaveEspacial("X-maxwell", "Alex", 300)

nave.recibir_disparo(100)   
nave.recargar_escudo(200)  
nave.recibir_disparo(500)   