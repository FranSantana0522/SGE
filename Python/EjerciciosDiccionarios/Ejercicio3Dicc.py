dic = dict(A='._',B='_...',C='_._.',CH='____',D='_..',E='.',F='.._.',G='__.',H='....',I='..',
           J='.___',K='_._',L='._..',M='__',N='_.',Ñ='__.__',O='___',P='.__.',Q='__._',
           R='._.',S='...',T='_',U='.._',V='..._',W='.__',X='_.._',Y='_.__',Z='__..')

codigoMorse = input("Codigo morse: ")

lista = codigoMorse.split(" ")
palabra = ""
for cod in lista:
    #letra = [key for key , valor in dic.items() if valor == cod][0]
    for key,valor in dic.items():
        if valor == cod:
            letra = key
            palabra = palabra + letra
print(palabra)

