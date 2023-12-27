import math
baseR = 4
ladoR = 2
perimetroR = baseR*2 + ladoR*2
print("Perimetro del rectangulo: "+ str(perimetroR)) 
areaR = baseR * ladoR
print("Area del rectangulo: "+ str(areaR))

radioC = 5
perimetroC = (radioC**2)*math.pi
print("Perimetro del circulo: %.2f" % (perimetroC))
areaC = ((radioC**2)*math.pi)/2*math.pi
print("Area del circulo: %.2f" % (areaC))