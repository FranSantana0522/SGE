numero = int(input("Introduce un numero: "))
fact = 1
for i in range(2,numero + 1):
    fact *= i
else:
    print("El factorial de ",numero," es ",fact)