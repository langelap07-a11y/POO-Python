class Transformer:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def transformarse(self) -> str:
        return f"{self.nombre} se transforma."


class AutobotCoche(Transformer):
    def transformarse(self) -> str:
        return f"{self.nombre}: ¡Se convierte en un deportivo a 300 km/h!"


class AutobotAvion(Transformer):
    def transformarse(self) -> str:
        return f"{self.nombre}: ¡Despliega las alas y vuela a velocidad supersónica!"


class AutobotDinosaurio(Transformer):
    def transformarse(self) -> str:
        return f"{self.nombre}: ¡Se transforma en un T-Rex robótico!"


autobots = [
    AutobotCoche("Bumblebee"),
    AutobotAvion("Jetfire"),
    AutobotDinosaurio("Grimlock"),
    AutobotCoche("Optimus Prime")
]

for autobot in autobots:
    print(autobot.transformarse())