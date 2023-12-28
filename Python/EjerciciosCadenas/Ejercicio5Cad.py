texto = input("Introduce palabra: ")

if texto.lower() == texto[::-1].lower():
    print("Es un palindromo")
else:
    print("No es un palindromo")