# > mayor
# >= mayor o igual
# == igual 
# <= menor o igual
# < menor
# and y
# or o
# ^ xor o(falso)
# elif se ejetuta solo si el if de arriba no se ejecuta
# continue en los bucles omite el codigo posterior e itera nuevamente
# for tiene un else que se ejecuta siempre y cuando no se dispare un break
# pass es para placeholder 

a = 5
b = 6
c = 7
nombres = ['Rodorigo', 'Benjamin', 'sas', 'Raul']
numeros = [1, 9, 6, 7, 5, 8, 2]

resultado = a > 4 and c > 6
resultadoOr = a < b or c > 10
resultadoXor = a < b ^ c > 10

print(resultado)
print(resultadoOr)
print(resultadoXor)

if a != 5 :
    a + 1
    print(a)
elif b != 6 :
    print('im in elif')
else :
    print('im in else')

contador = 0

while contador <= 10 :
    print('Tengo ', contador, ' manos')
    if contador % 2 == 0 :
        print(contador, ' es par')
    if contador == 9 :
        break
    contador += 1

for nombre in nombres :
    print('Hola ', nombre)

for numero in range(10, 30) :
    print(numero)

if 'Rodorigo' in nombres :
    print('hola Rodo')

print(sorted(numeros))
print(sorted(numeros, reverse=True))

valorSwitch = 4

match valorSwitch :
    case 1 :
        print('valor es uno')
    case 2 :
        print('valor es dos')
    case 3 :
        print('valor es tres')
    case 4 :
        print('valor es cuatro')
    case 5 :
        print('valor es cinco')