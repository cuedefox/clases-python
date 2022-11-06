class Vehiculo:
    color = None
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

corsa = Coche('Rojo', 4, 4, 180, 'No se de coches :D')

print(corsa.color, corsa.ruedas, corsa.velocidad)