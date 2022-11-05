# Realizo funcion que te dice si el año es biciesto o no

def anioBiciesto(anio) :
    mensaje = ""
    if anio % 4 == 0:
        mensaje = "Es anio biciesto"
    else:
        mensaje = "No es anio biciesto"
    return mensaje
    
print(anioBiciesto(2008))