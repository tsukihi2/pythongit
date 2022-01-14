valor = int(input('qual o valor em m?\n'))
valorkm = valor/1000
valorhecm = valor/100
valordecm = valor/10
valordm = valor*10
valorcm = valor*100
valormm = valor*10000
print('o valor em km é: {}\n o valor em hectometros é {}\n o valor em decametros é {}\n o valor em dm{}\n o valor em cm{}\n o valor em mm{}\n'.format(
    valorkm, valorhecm, valordecm, valordm, valorcm, valormm))
