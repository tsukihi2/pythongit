salario = float(input('qual o salário de um funcionario?\n'))
aumento = float(input('qual o valor do aumento?\n'))
resultado = salario + (salario*(aumento/100))
print('o salario de {} com {}% de aumento fica em {}'.format(
    salario, aumento, resultado))
