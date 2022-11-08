import time

def irCasa():
    hora = time.strftime("%H")
    if int(hora) >= 7:
        return "volver a casa, son las ", hora
    else:
        quedan = 7 - int(hora)
        return "quedan ", quedan, " horas de trabajo"

print(''.join(irCasa()))