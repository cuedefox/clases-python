from functools import reduce
numeros = [5, 7, 9, 6, 3, 2, 1, 4]

resultado = filter(lambda x: x % 2 == 0, numeros)
print(list(resultado))

resultado2 = map(lambda x: x * x, numeros)
print(list(resultado2))

resultado3 = reduce(lambda a, b: a + b, numeros)
print(resultado3)