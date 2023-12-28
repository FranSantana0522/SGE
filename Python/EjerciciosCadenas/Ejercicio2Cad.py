texto = input("Introduce texto: ")
caracter = input("Introduce caracter: ")

for i in range(10):
    texto = texto.replace(str(i),caracter)
print(texto)