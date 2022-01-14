print('Bem vindo ao calculador de calorias diarias')
print('Note que os valores daqui não tem uma fonte cientifica clara mas contém uma estimativa aproximada')
print('Primeiro vamos ao seu gênero')
gen = int(input('Digite 1 se for homem ou 2 se for mulher\n'))
idade = int(input('Qual sua idade?\n'))
peso = int(input('Qual seu peso?\n'))

if((idade >= 18) & (idade <= 30) & (gen == 1)):
    resultado = ((0.063*peso) + 2.896)*239
    print(resultado)
    #print('vc é um homem de peso: {}kg e idade: {}'.format(peso, idade))
elif ((idade >= 18) & (idade <= 30) & (gen == 2)):
    resultado = ((0.062*peso) + 2.036) * 239
    print(resultado)
    #print('vc é uma mulher de peso: {}kg e idade: {}'.format(peso, idade))
elif ((idade >= 30) & (gen == 1)):
    resultado = ((0.048 * peso) + 3.653) * 239
    print(resultado)
    #print('vc é um homem de peso {}kg e idade: {} '.format(peso, idade))
elif((idade >= 30) & (gen == 2)):
    resultado = ((0.034 * peso) + 3.538) * 239
    print(resultado)
    #print('vc é uma mulher de peso {}kg e idade {}'.format(peso, idade))
else:
    print('valor invalido burro nice try')
