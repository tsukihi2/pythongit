d = int(input('quantos dias o carro ficou com voce?\n'))
km = float(input('quantos kms foram rodados?\n'))
resultado = d*60 + 0.15*km
print('o valor a se pagar é de {}'.format(resultado))
