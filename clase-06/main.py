# en python si una propiedad o metodo comienza por _ no se debe manipular desde fuera

# self. se llama como parametro y antes de la propiedad en los metodos para manipular las
#variables dentro de un objero

# las clases estaticas comparten zona de memoria

# se pueden concatenar herencias

# el desctructor se utiliza cuando finaliza el programa para limpiar memoria

# se tiene que heredar el constructor de la clase padre con super().__init__(parametros)

# las clases en python son diccionarios

# para importar clases abstractas se utiliza:
from abc import ABC, abstractmethod

# no se puede instanciar una clase abstracta, se deriva para instanciarla, sirve para 
#definir un conjunto de funciones comunes a otras clases

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

# los metodos abstractos deben ser utilizados por los hijos si o si

class Persona:
    nombre = None
    edad = None

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print('destruimos', self.__class__)

    def cumplirAnios(self):
        self.edad += 1

rodri = Persona('Rodrigo', 21)
print(rodri.edad)
rodri.cumplirAnios()
print(rodri.edad)

class Estatica:
    contador = 0
    def incrementar():
        Estatica.contador += 1
        print(Estatica.contador)

Estatica.incrementar()
Estatica.incrementar()
Estatica.incrementar()
Estatica.incrementar()

# herencia (is a)

class Gemelo(Persona):
    lunares: None
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

roxi = Gemelo('Roxana', 21)
roxi.cumplirAnios()
print(roxi.edad)

class Perro(Animal):
    def sonido(self):
        print('guau')

piyo = Perro()

piyo.sonido()

# las clases pueden ser compuestas, contener instancias de otras clases (has a)

class Ventanas:
    cantidad = 4

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Motor:
    tipo = 'Diesel'

class Coche:
    carroceria = Carroceria()
    motor = Motor()

mio = Coche()

print(mio.carroceria.ruedas.cantidad)