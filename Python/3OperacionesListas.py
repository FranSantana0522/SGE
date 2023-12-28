# 1 list(map(int,nombrelista)) si la lista tiene caracteres numericos en " " con esta funcion los transformamos a int todas a la vez
#       tambien puedes usar funciones list(map(funcion,nombrelista)) introduce los elementos de la lista en la funcion y los devuelve 
#       a la lista

# 2 list(filter(funcion,nombrelista)) filtra los elementos de la lista que devuelva la funcion

# 3 reduce para usar reduce se debe poner " from functools import reduce " reduce(funcion,nombrelista) la funcion devuelve un elemento
#       por ejemplo un funcion de suma haria que la lista [1,2,3,4] -> reduce(sumar,lista) devuelve 10

# 4 listas comprimidas -> [ x ** 3 for x in [1,2,3,4,5] ] devuelve una lista de los cubos de la lista de dentro
#                      -> [ x for x in range(10) if x % 2 == 0 ] devuelve una lista con solo los pares
#                      -> [ x + y for x in [1,2,3] for y in [4,5,6] ] devuelve una lista con la suma de cada elemento de la lista 1 con
#                                                                     los otros elementos de la lista 2