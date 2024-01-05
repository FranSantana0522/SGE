def segundosTotal(horas,minutos,segundos):
    minutos += horas * 60
    segundos += minutos * 60
    print(segundos,' segundos')

def horaCompleta(segundos):
    minutos = int(segundos / 60)
    segundos = int(segundos % 60)
    horas = int(minutos / 60) 
    minutos = int(minutos % 60)
    if horas < 0:
        horas = 0
    print(horas,'h ',minutos,'m ',segundos,'s')

def calculoTiempo(*args):
    if len(args) == 1:
        horaCompleta(args[0])
    elif len(args) == 3:
        segundosTotal(*args)
    else:
        raise TypeError("Se espera 1 o 3 argumentos")
    
if __name__ == '__main__':
    calculoTiempo(4,3,6)
