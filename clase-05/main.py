nombre = 'roberto'

# es necesario declarar global en una variable en una funcion para que el scope sea global

def funcion(render):
    global nombre
    nombre = 'rodrigo'
    print('imprimiste:', render)

def sumar(a, b):
    return a + b

# se inicializa un parametro para darle un valor predeterminado en las funciones

def sumarTres(a=3, b=4, c=8):
    print('resultado:', a + b+ c)

def saludar(nombre='anonimo'):
    print('hola', nombre)

# *args = parametros variables crea una tupla

def acumular(*args):
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)

# **kwargs = parametro variable, crea un diccionario

def crearDiccionario(**kwargs):
    for key, value in kwargs.items():
        print(key, '=', value)

def operaciones(a, b):
    return a + b, a - b, a * b, a / b

# se suele usar el _ para ignorar el valor de retorno, al haber muchos returns, se le asigna
# una variable a cada uno o se asignan todos a una variable del cual sera una tupla

funcionAnonima = lambda nombre : print('Hola', nombre)

suma, resta, multi, divi = operaciones(60, 5)

funcion('hola')
funcion('My name is gustavo')
resultadoSuma = sumar(4, 50)
print(resultadoSuma)
print(nombre)
saludar()
sumarTres(b=10)
acumular(15, 53, 1, 9, 57, 87, 12, 20)
crearDiccionario(nombre = "rodrigo", edad = 21)
print(suma)
print(resta)
print(multi)
print(divi)
funcionAnonima("perro")