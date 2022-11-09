f = open("C:/Users/Rodrigo Vergara/Documents/Programacion/6.Python/clases-python/clase-08/hola.txt", 'r')
r = open("C:/Users/Rodrigo Vergara/Documents/Programacion/6.Python/clases-python/clase-08/datos.txt", 'w')
# r : lectura
# a : append, añade al final
# w : escritura
# x : create

# t : texto
# b : binary

datos = f.read()
f.close()

lineas = [
    "una linea \n",
    "dos lineas \n",
    "tres lineas \n"
]

r.write("datos \n")
r.write("datos2 \n")
r.writelines(lineas)
r.close

print(datos)