gustos={}
nombre = input("Nombre: ")

while nombre != "*" :
    gusto = input("Gusto: ")
    listaGustos = gustos.setdefault(nombre, [gusto])
    if listaGustos != [gusto]:
        gustos[nombre].append(gusto)
    nombre = input("Nombre: ")
print(gustos)
