class Alumno:
    nombre = None
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def evaluar(self):
        if self.nota >= 7:
            print('Felicidades', self.nombre, 'aprobaste con un', self.nota)
        else:
            print('Que mal', self.nombre, 'desaprobaste con un', self.nota)

rodrigo = Alumno('Rodrigo', 4)

rodrigo.evaluar()