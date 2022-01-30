from random import shuffle
n1 = str(input('digite um nome '))
n2 = str(input('digite o segundo nome '))
n3 = str(input('digite o terceiro nome '))
n4 = str(input('digite o quarto nome '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('nova ordem é')
print(lista)
