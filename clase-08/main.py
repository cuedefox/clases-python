# hasta 3.6 usar:

numero = 115
string = "Rodrigo"

print("A {} le gusta el {}".format(string, numero))
print("A {1} le gusta el {0}".format(string, numero))
print("A {nombre} le gusta el {numero}".format(nombre = string, numero = numero))

# usar asi

print(f'A {string} le gusta el {numero}') 

# str() para usuario repr() para desarrollo

# tambien esta __repr__ como metodo para las clases, en las que se puede establecer 
#la salida

class juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f'Hola soy {self.nombre} y valgo {self.precio}'

anakin = juguete("Anakin", 20000.0)
demo = str(anakin)

print(anakin)
print(demo)
print(repr(anakin))

# metodos cadenas

cadena = "hace mucho tiempo en una galaxia muy muy lejanA..."
numeroStr = "40"

print(cadena.capitalize())
print(cadena.title())
print(cadena.count('a'))
print(cadena.lower())
print(cadena.upper())
print(numeroStr.isdigit())
print(cadena.split())
print(cadena.split('a'))
print(cadena.startswith('hace'))