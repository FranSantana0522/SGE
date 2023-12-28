# LAS CADENAS SON INMUTABLES NINGUNO DE LOS METODOS MODIFICA LA CADENA ORIGINAL
# 1 cad.upper() convierte los caracteres a mayusculas para modificarlo seria asi cad=cad.upper()

# 2 cad.capitalize() pone la primera letra en mayusculas

# 3 cad.lower() convierte la cadena a minusculas

# 4 cad.swapcase() devuelve la cadena con las minusculas y mayusculas intercambiadas

# 5 cad.title() devuelve la cadena con los primeros caracteres de cada palabra en mayusculas

# 6 cad.center(50) centra la cadena el numero son los espacios otra manera es .center(50,"=") y coloca = en vez de espacios

# 7 cad.ljust(50) alinea a la izquierda y lo mismo con center puedes cambiar los espacios por otro caracter

# 8 cad.rjust(50) alinea a la derecha      "    "   "   "   "   "   "   "   "   "   "   "   "   "   "   "

# 9 "123".zfill(12) coloca 0 desde el ultimo caracter sin cambiarlos hacia la izquierda se veria asi 000000000123

# 10 cad.count(caracter) cuenta cuantas veces aparece un caracter, tambien se puede indicar la posicion desde cual comenzar

# 11 cad.find(caracter o subcadena) devuelve el indice donde se encuentra el caracter o una subcadena
#    cad.rfind busca desde la derecha

# 12 cad.index(caracter) devuelve el indice donde se encuentra el caracter

# 13 cad.startswith(subcadena o caracter) devuelve true or false si empieza asi la cadena o no, tambien si una subcadena en una 
#                                         cierta posicion empiza asi

# 14 cad.endwith(subcadena o caracter) lo mismo que startswith

# 15 format -> "{} {}".format("a","b") tambien se pueden poner posiciones en las llaves tambien podemos darle claves 
#           -> 'Coordenadas: {Latitud}, {Longitud}'.format(Latitud='37.24N', Longitud='-115.81W')
#              tambien se puede indicar el formato que se quiere como salida en las laves {0:b} {1:x} {2:.2f}

# 16 cad.replace(caracter a cambiar, caracter que reemplaza) tambien funciona con subcadenas

# 17 cad.strip() devuelve una cadena sin espacios rstrip() por la derecha y lstrip() por la izquierda pa quitar espacios, tambien puede
#                eliminar cualquier caracter 

# 18 join -> una tupla formato = ("Nº 0000-0", "-0000  (ID: ", ")") y ahora le hacemos un print("275".join(formato)) el resultado sera
#            Nº 0000-0275-0000 (ID: 275) basicamente la tupla la usamos como una plantilla y la cadena que metemos se inserta en los 
#                                        espacios

# 19 cad.partition(caracter separador) separa la cadena por el caracter indicado si el caracter separador se repite solo separa por 
#                                      el primero que encuentre

# 20 cad.split(caracter separador) separa la cadena pero no incluye el separador, tambien separa todo sin importar cuantas veces se 
#                                  repita el separador

# 21 cad.splitlines() devuelve de un texto con varias lineas cada linea separada