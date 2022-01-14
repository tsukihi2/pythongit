preço = float(input('qual o preço do produto?\n'))
desconto = float(input('qual o valor do desconto em %?\n '))
resultado = preço*((100-desconto)/100)
print('o preço do produto de {} com {}% de desconto é de {} '.format(
    preço, desconto, resultado))
