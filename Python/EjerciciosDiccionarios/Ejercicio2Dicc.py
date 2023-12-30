dic = dict(A=' . _ ',B=' _ . . . ',C=' _ . _ . ',CH=' _ _ _ _ ',D=' _ . . ',E=' . ',F=' . . _ . ',G=' _ _ . ',H=' . . . . ',I=' . . ',
           J=' . _ _ _ ',K=' _ . _ ',L=' . _ . .',M=' _ _ ',N=' _ . ',Ñ=' _ _ . _ _ ',O=' _ _ _ ',P=' . _ _ . ',Q=' _ _ . _ ',
           R=' . _ . ',S=' . . . ',T=' _ ',U=' . . _ ',V=' . . . _ ',W=' . _ _ ',X=' _ . . _ ',Y=' _ . _ _ ',Z=' _ _ . . ')

palabra = input("Introduce una palabra: ")
lista = []
for letra in palabra :
    letra=letra.upper()
    lista.append(dic[letra])
print (" ".join(lista))