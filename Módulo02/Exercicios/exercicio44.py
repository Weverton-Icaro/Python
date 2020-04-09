print('O produto custa R$200,00.')
valorP = 200

print(''''Escolha uma forma de pagamento:
[ 1 ] Dinheiro ou cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''''')

op = int(input('Qual será? '))
if(op) == 1:
  soma1 = valorP - ((valorP *10) /100)
  print('O valor pago deu desconto de 10%, o valor do produto ficou em R${:.2f}.'.format(soma1))
elif(op) == 2:
  soma2 = valorP - ((valorP *5) / 100)
  print('O valor pago deu desconto de 5%, o valor do produto ficou em R${:.2f}.'.format(soma2))
elif(op) == 3:
  print('O valor pago do produto foi R${:.2f}.'.format(valorP))
elif(op) == 4:
  soma3 = valorP + ((valorP *20)/100)
  print('O valor pago no produto foi de R${:.2f}.'.format(soma3))