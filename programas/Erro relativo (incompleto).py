valoresperado = int(input("Qual o valor esperado?\n"))
valorobtido = int(input("Qual o valor obtido?\n"))
err = (abs(valorobtido-valoresperado)/valoresperado)*100
print('O erro relativo é de {}%'.format(err))
