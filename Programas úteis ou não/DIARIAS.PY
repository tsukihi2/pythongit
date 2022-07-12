import pandas as pd
import numpy as np
print('BEM VINDO AO PROGRAMA DE ORGANIZAÇÃO DE DIARIAS')
print('SAIBA QUE ESSE PROGRAMA USA UM ESQUEMA DE FAZER AS DIARIAS 3X NA SEMANA PRA CADA ALT')
print('logo será formado uma tabela q divide a semana de SEGUNDA a SABADO')
print('VAMOS LÁ')

listadealts = list()
alt = dict()
while True:
    alt.clear()
    alt['Nick'] = str(input('NICK DA ALT '))
    alt['iLVL'] = int(input('QUAL O iLVL DESSA ALT '))
    listadealts.append(alt.copy())
    while True:
        resp = str(input('QUER CONTINUAR??? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR RESPONDA APENAS COM S OU N ANIMAL...')
    if resp == 'N':
        break
print('='*30)
numalts = len(listadealts)
# print(numalts)

coluna = 'SEG TER QUAR QUI SEX SAB DOM'.split()
linha = list()
for c in range(1, numalts+1):
    linha.append(c)

tabela = pd.DataFrame(index=linha, columns=coluna)
