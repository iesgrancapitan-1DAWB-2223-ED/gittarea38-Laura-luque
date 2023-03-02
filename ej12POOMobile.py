from ej11POOTerminal import Terminal
class Mobile(Terminal):
    tarifas = {"rata": 0.06, "mono": 0.12, "bisonte": 0.30}

    def __init__(self, id, tarifa):
        super().__init__(id)
        self.tarifa = tarifa
        self.coste_total = 0.0

        if tarifa not in self.tarifas:
            raise ValueError("Tarifa no válida")

    def cambiar_tarifa(self, nueva_tarifa):
        if nueva_tarifa not in self.tarifas:
            raise ValueError("Tarifa no válida")
        self.tarifa = nueva_tarifa

    def obtener_coste_llamada(self, duracion):
        return round(duracion / 60 * self.tarifas[self.tarifa], 2)

    def llamar(self, other, duracion):
        coste_llamada = self.obtener_coste_llamada(duracion)
        super().call(other,duracion)
        self.coste_total += coste_llamada

    def __str__(self):
        return f"Nº {self.id[0:3]} {self.id[3:5]} {self.id[5:7]} {self.id[7:9]} - {self.tiempoConversacion}s de conversación - tarificados {self.coste_total:.2f} euros"
