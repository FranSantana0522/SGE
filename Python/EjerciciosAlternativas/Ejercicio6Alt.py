caracter = str(input("Introduce un caracter: "))

if caracter>='A' and caracter<='Z':
    print("Mayusculas")
elif caracter>='a' and caracter<='z':
    print("Minusculas")
else:
    print("Otro caracter")