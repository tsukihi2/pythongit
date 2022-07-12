from scipy import constants
from scipy.constants import pi as p
from scipy.constants import elementary_charge as e
import numpy
print('bem vindo a calculadora de ciencia dos materiais')
print('Primeiramente vamos checar qual calculadora vc quer usar\n')
resposta = input('1-FORÇA DE ATRAÇÃO\n2-xxxx\n3-yyyyy\n')
if(resposta == '1'):
    num3 = '='
    print('==={:=^60}'.format(num3))
    ion1 = float(input('Qual a carga do primeiro ion em módulo:\n'))
    ion2 = float(input('Qual a carga do segundo ion:\n'))
    dist = float(input('qual a distância entre os núcleos em nm\n'))
    ezero = constants.value('vacuum electric permittivity')
    num3 = '='
    print('==={:=^60}'.format(num3))
    fa = (ion1*ion2*e**2)/(4*p*ezero*((dist*1e-9)**2))
    print('O VALOR DA FORÇA DE ATRAÇÃO ENTRE ELES É DADO POR \n {} N' .format(fa))
else:
    print('ainda nao tem essa burro')
