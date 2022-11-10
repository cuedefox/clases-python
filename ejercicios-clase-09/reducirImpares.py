from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def reducir(arr):
    impar = filter(lambda x: x % 2, arr)
    return reduce(lambda a, b: a + b, impar)

print(reducir(numeros))