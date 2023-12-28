lista = ["hola","que","tal","wasap"]
print(lista)
esta = input("Introduce una cadena: ")
lista.append(esta)
print(lista)
print("Aparece en la lista ",lista.count(esta)," veces")
esta2 = input("Introduce una cadena: ")

apariciones = lista.count(esta)
pos=0
for i in range(0,apariciones) :
    pos=lista.index(esta,pos)
    lista[pos]=esta2
else: 
    print(lista)