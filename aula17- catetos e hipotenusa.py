#from math import hypot
#valorCO = float(input('Comprimento do cateto oposto: '))
#valorCA = float(input('Comprimento do cateto adjacente: '))
#hip = hypot(valorCO, valorCA)
#print(f'A hipotenusa vai medir {hip:.2f}')

from math import sqrt, pow
valorCO = float(input('Comprimento do cateto oposto: '))
valorCA = float(input('Comprimento do cateto adjacente: '))
hip = sqrt(pow(valorCO, 2) + pow(valorCA, 2))
print(f'A hipotenusa vai medir {hip:.2f}')