import pickle

class vehiculo:
    nombre = 'Runr RUNAUSNAUSNAus'

coche = vehiculo()

f = open("C:/Users/Rodrigo Vergara/Documents/Programacion/6.Python/clases-python/ejercicios-clase-08/data.bin", 'wb')
pickle.dump(coche, f)
f.close()

f = open("C:/Users/Rodrigo Vergara/Documents/Programacion/6.Python/clases-python/ejercicios-clase-08/data.bin", 'rb')
insta = pickle.load(f)
f.close()

print(insta.nombre)