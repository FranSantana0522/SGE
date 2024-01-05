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

if __name__ =='__main__':
    segundosTotal(12,30,20)
    horaCompleta(24302)