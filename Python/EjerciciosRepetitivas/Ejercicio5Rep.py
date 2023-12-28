num = int(input("Introduce un numero: "))
primo = False
while primo != True :
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        print(num," es primo")
        primo = True
    else: 
        print(num," no es primo")
        num = int(input("Introduce un numero: "))