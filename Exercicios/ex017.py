from math import sqrt
ca = float(input('qual o valor do cateto adjacente: '))
co = float(input('qual o valor do cateto oposto: '))
result = sqrt((co**2)+(ca**2))
print('o valor da hipotenusa é = {}'.format(result))
