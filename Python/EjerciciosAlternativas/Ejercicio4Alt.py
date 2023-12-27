user = "Pepe"
password = "12345"

nombre = str(input("Introduce nombre usuario: "))
contraseña = str(input("Introduce contraseña del usuario: "))
flag = None
if nombre == user :
    flag = True
else:
    print("Nombre de usuario mal introducido")

flag2 = None
if contraseña == password:
    flag2 = True
else:
    print("Contraseña mal introducida")

if flag == True and flag2 == True:
    print("Inicio de sesion correcto")
