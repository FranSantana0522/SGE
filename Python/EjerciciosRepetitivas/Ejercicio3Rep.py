import os
numSec = int(input("Introduce un numero secreto: "))
os.system("cls")
cont = 1
numAdv = int(input("Introduce numero: "))
while numAdv != numSec :
    if numAdv > numSec :
        print("El numero secreto es menor")
    else :
        print("El numero secreto es mayor")
    cont += 1 
    numAdv = int(input("Introduce numero: "))
print("Has ganado en ",cont," intentos")  