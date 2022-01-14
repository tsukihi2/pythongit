print('Bem vindo ao macromaker\n')
print('Primeiramente vamos checar os botões que vc aperta o A, B, fatal\n')
print('{:=^40}')
num3 = '='
print('==={:=^60}'.format(num3))
# OBTER O BOTÃO QUE A PESSOA USA O A
butA = str(input("Qual o botão que vc usa o ataque A? \n"))
# OBTER O BOTÃO QUE A PESSOA USA O B
butB = str(input("Qual o botão que vc usa o ataque B?\n"))
# OBTER O BOTÃO QUE A PESSOA USA O FATAL
butF = str(input("Qual o botão que vc usa o FATAL?\n"))

print('==={:=^60}'.format(num3))

print('Agora vamos checar quais os cast times dos ataques A B e fatais 1, 2 3; \n')

print('==={:=^60}'.format(num3))

# OBTER BOTAO QUE A PESSOA USA ATAQUE A
castA = float(input('Qual o cast time do ataque A?\n'))
castFA = castA+0.180
# OBTER BOTAO QUE A PESSOA USA ATAQUE B
castB = float(input('Qual o cast time do ataque B?\n'))
castFB = castB+0.180
# OBTER BOTAO QUE A PESSOA USA ATAQUE FATAL 1
castF1 = float(input('Qual o cast time do FATAL 1?\n'))
castFf1 = castF1+0.180
# OBTER BOTAO QUE A PESSOA USA ATAQUE FATAL 2
castF2 = float(input('Qual o cast time do FATAL 2?\n'))
castFf2 = castF2+0.180
# OBTER BOTAO QUE A PESSOA USA ATAQUE FATAL 3
castF3 = float(input('Qual o cast time do FATAL 3?\n'))
castFf3 = castF3+0.180

print('==={:=^60}'.format(num3))

resposta = input(
    'digite 1 sinergia optimzada pra sua classe ou 2 para criação propria sua\n')
if (resposta == '1'):
    profess = input('Qual a sua classe?\n')
    if (profess == 'MA' or profess == 'ma' or profess == 'Ma' or profess == 'mago'):
        print('SINERGIA PRA {}\n'.format(profess))
        print('ABAA BBAB BAAB\n')
        print('butB{WAIT:castFB}butB{WAIT:castFB}butA{WAIT:castFA}butB{WAIT:castFB} butA{WAIT:castFA}butB{WAIT:castFB}butA{WAIT:castFA}butA{WAIT:castFA} butB{WAIT:castFB}butA{WAIT:castFA}butA{WAIT:castFA}butB{WAIT:castFB}')
        wait = input('pressione algo para finalizar')
    elif (profess == 'DU' or profess == 'du' or profess == 'Du' or profess == 'duelista'):
        print('SINERGIA PRA {}'.format(profess))
    elif (profess == 'GU' or profess == 'gu' or profess == 'Gu' or profess == 'guerreiro' or profess == 'guerrero'):
        print('SINERGIA PRA {}'.format(profess))
    elif (profess == 'GA' or profess == 'ga' or profess == 'Ga' or profess == 'guardião'):
        print('SINERGIA PRA {}'.format(profess))
    elif (profess == 'GL' or profess == 'gl' or profess == 'Gl' or profess == 'gladiador'):
        print('SINERGIA PRA {}'.format(profess))
    elif (profess == 'EA' or profess == 'ea' or profess == 'Ea' or profess == 'espadachim' or profess == 'espadachin'):
        print('SINERGIA PRA {}'.format(profess))
    elif (profess == 'AA' or profess == 'aa' or profess == 'Aa' or profess == 'arqueiro' or profess == 'arquero'):
        print('SINERGIA PRA {}'.format(profess))
    elif (profess == 'AT' or profess == 'at' or profess == 'At'):
        print('SINERGIA PRA {}'.format(profess))
else:
    string = str(input(
        'QUAL SEQUENCIA DE SINERGIA VC QUER FAZER; EXAMPLE BBABBAAB(use esse formato sem espaços):\n'))
    replaceA = string.replace("A", butA)
    replaceB = replaceA.replace("B", butA)
    print(replaceB)
