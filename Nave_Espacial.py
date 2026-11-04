class NaveEspacial:
    def __init__(self, nombre: str, piloto: str, nivel_escudo: int):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo


nave1 = NaveEspacial("Halcón pollero", "Alex", 200)
nave2 = NaveEspacial("X-maxwell", "Manson", 300)

print(f"Nave 1 - Nombre: {nave1.nombre}, Piloto: {nave1.piloto}, Nivel de escudo: {nave1.nivel_escudo}")
print(f"Nave 2 - Nombre: {nave2.nombre}, Piloto: {nave2.piloto}, Nivel de escudo: {nave2.nivel_escudo}")
    


    
