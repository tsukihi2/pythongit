import random
for k in range(1, 10):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    print('multiplique:')
    print('{} x {} '.format(a, b))
    c = a*b
    print(c)
    resposta = int(input('resposta = '))
    if(resposta == c):
        # print(c)
        print('acertou cara')
    else:
        print('errou sadge')
        print('repsosta correta = a {}' .format(c))
print('bom treino mano')
print('vc fez {} tentativas!!'.format(k))
