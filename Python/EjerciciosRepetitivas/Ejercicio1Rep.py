num = int(input("Introduce numero: "))
i = 0
while i<11:
    print(num," x ", i, " = ",num*i) 
    i += 1
else:
    print("Bucle while\n")

for j in range(11):
    print(num," x ", j, " = ",num*j) 
else:
    print("Bucle for\n")

