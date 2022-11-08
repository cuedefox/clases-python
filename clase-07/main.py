# __name__ da el nombre del modulo, si no es importado se llamara main
# sys.path devuelve la ruta del modulo
# un paquete es una coleccion de modulos
# con dir() se ven los metodos de un objeto
# globals() devuelve la tabla de simbolos global, locals() la local

import operaciones as op
from operations.divmulti import divi
from operations.divmulti import multi
import sys
import pprint

def main(a, b):
    sum = op.suma(a, b)
    res = op.resta(a, b)
    div = divi.divi(100, 15)
    mult = multi.multi(5, 10)
    print(sum, res, div, mult)

if __name__ == '__main__':
    main(60, 20)

pprint.pprint(sys.path)
pprint.pprint(globals())