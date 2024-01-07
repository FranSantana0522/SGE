
def guardarAgenda(l_agenda,**kwargs):
    resultado=l_agenda[:]
    resultado.append(kwargs)
    return resultado

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

if __name__=='__main__':
    main()