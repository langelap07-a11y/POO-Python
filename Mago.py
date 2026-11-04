class Mago:
    def __init__(self, nombre: str, mana_base: int):
        self.nombre = nombre
        self.mana_base = mana_base


class MagoFuego(Mago):
    def __init__(self, nombre: str, mana_base: int, temperatura_llama: int):
        super().__init__(nombre, mana_base)
        self.temperatura_llama = temperatura_llama

    def lanzar_bola_fuego(self) -> None:
        costo = 20
        if self.mana_base >= costo:
            self.mana_base -= costo
            print(f"{self.nombre} lanza una bola de fuego a {self.temperatura_llama}°C. Maná restante: {self.mana_base}")
        else:
            print(f"{self.nombre} no tiene maná suficiente para lanzar una bola de fuego.")


class MagoHielo(Mago):
    def __init__(self, nombre: str, mana_base: int, grosor_escudo_hielo: int):
        super().__init__(nombre, mana_base)
        self.grosor_escudo_hielo = grosor_escudo_hielo

    def congelar_terreno(self) -> None:
        costo = 30
        if self.mana_base >= costo:
            self.mana_base -= costo
            print(f"{self.nombre} congela el terreno con un escudo de hielo de {self.grosor_escudo_hielo} cm. Maná restante: {self.mana_base}")
        else:
            print(f"{self.nombre} no tiene maná suficiente para congelar el terreno.")


mago_fuego = MagoFuego("Ignis", 50, 1200)
mago_hielo = MagoHielo("Glacia", 60, 15)

mago_fuego.lanzar_bola_fuego()
mago_fuego.lanzar_bola_fuego()
mago_fuego.lanzar_bola_fuego()

mago_hielo.congelar_terreno()
mago_hielo.congelar_terreno()
mago_hielo.congelar_terreno()