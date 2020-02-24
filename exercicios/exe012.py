#Mostra preço de produto com 5% de desconto
n1 = float(input('Qual o valor da mercadoria? '))
n2 = n1 * 5
n3 = n2 / 100
s = n1 - n3
print('O valor da mercadoria é {}, o valor do desconto de 5% foi de {}'.format(s, n3))
