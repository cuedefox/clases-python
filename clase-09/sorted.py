lista = ['c', 'e', 'a', 'b', 'r']

ordenada = sorted(lista, reverse=False)
ordenada2 = sorted(lista, reverse=True, key= lambda x: str(x).startswith('a'))

print(ordenada)
print(ordenada2)