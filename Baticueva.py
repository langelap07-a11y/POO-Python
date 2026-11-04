class BatcuevaSystem:
    def __init__(self, mando_central_pass: str, nivel_alerta: str = "Verde"):
        self.__mando_central_pass = mando_central_pass
        self.__nivel_alerta = nivel_alerta

    def obtener_alerta(self) -> str:
        return self.__nivel_alerta

    def cambiar_alerta(self, nueva_alerta: str, clave_ingresada: str) -> bool:
        if clave_ingresada == self.__mando_central_pass:
            self.__nivel_alerta = nueva_alerta
            print(f"Acceso concedido. Nivel de alerta cambiado a: {nueva_alerta}")
            return True
        else:
            print("Acceso denegado. Clave incorrecta.")
            return False


sistema = BatcuevaSystem("Alfred123", "Verde")

print(f"Alerta inicial: {sistema.obtener_alerta()}")

sistema.cambiar_alerta("Rojo", "Alfred123")
print(f"Alerta actual: {sistema.obtener_alerta()}")

sistema.cambiar_alerta("Amarillo", "clave_falsa")
print(f"Alerta actual: {sistema.obtener_alerta()}")