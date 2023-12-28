cad = "hola wenas tardes soy aderraman"

lista = cad.split(" ")
for palabra in lista:
    print(palabra[0],end="")
print()
print(cad.title())

for palabra in lista:
    if palabra.startswith('a') or palabra.startswith('A'):
        print(palabra,sep=", ")