cad = input("Introduce una cadena: ")

lista=cad.split(" ")
dic = {}

for palabra in lista :
    if palabra in dic:
        dic[palabra]+=1
    else:
        dic[palabra]=1
        
for k,v in dic.items():
    print(k," -> ",v)