num = int(input("Introduce un numero: "))
lista=[]
while num>=0 :
    lista.append(num)
    num = int(input("Introduce un numero: "))
else:
    print("El maximo es: ",max(lista))
print("Numero pares de la lista: ",end=" ")
for i in lista :
    if i % 2 == 0 :
        print(i,end=" ")