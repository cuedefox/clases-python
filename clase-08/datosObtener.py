class juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f'Hola soy {self.nombre} y valgo {self.precio}'

import pickle
f = open("C:/Users/Rodrigo Vergara/Documents/Programacion/6.Python/clases-python/clase-08/data.bin", 'rb')
j1 = pickle.load(f)
f.close()

print(type(j1))
print(j1.nombre)