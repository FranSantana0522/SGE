mes = int(input("Introduce numero del 1 al 12: "))
while mes > 12 or mes < 1 :
    mes = int(input("Introduce numero del 1 al 12: "))

if mes <= 7:
    if mes == 2:
        print("28")
    elif mes % 2== 0:
        print("30")
    else:
        print("31")
else:
    if mes % 2 == 0:
        print("31")
    else:
        print("30")