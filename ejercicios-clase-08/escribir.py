f = open("C:/Users/Rodrigo Vergara/Documents/Programacion/6.Python/clases-python/ejercicios-clase-08/nota.txt", 'w')
lista = [
    'Rodrigo',
    'Lucia',
    'Dante',
    'Luz'
]

for nombre in lista:
    if not nombre.endswith('\n'):
        nombre += '\n'
    f.write(nombre)

f.close