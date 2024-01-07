
def guardarAgenda(l_agenda,**kwargs):
    resultado=l_agenda[:]
    resultado.append(kwargs)
    return resultado

def buscar(l_agenda,**kwargs):
    listaAciertos = []
    for contacto in l_agenda:
        aciertos=0
        for campo,valor in kwargs.items():
            if campo in contacto and contacto[campo] == valor:
                aciertos+=1
        if aciertos==len(kwargs):
            listaAciertos.append(contacto)
    return listaAciertos

def main():
    agenda = []
    cantidad=int(input("Cantidad de contactos a agendar: "))
    for i in range(cantidad):
        contacto={}
        contacto["nombre"]=input("Introduce nombre del contacto: ")
        contacto["telefono"]=input("Introduce telefono del contacto: ")
        campo=input("Introduzca otro campo de la agenda: ")
        while campo !="*":
            contacto[campo]=input("Introduzca el valor: ")
            campo=input("Introduzca otro campo de la agenda: ")
        agenda=guardarAgenda(agenda,**contacto)[:]
    print(agenda)

    filtro={}
    campo=input("Introduca un campo para buscar: ")
    while campo !="*":
        filtro[campo]= input("Introduzca el valor: ")
        campo=input("Introduca un campo para buscar: ")
    print(buscar(agenda,**filtro))

if __name__=='__main__':
    main()