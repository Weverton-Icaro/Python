num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if(num1 > num2):
  print('O primeiro valor {} é maior que {}.'.format(num1, num2))
elif(num1 < num2):
  print('O segundo valor {} é maior que {}.'.format(num2, num1))
else:
  print('Não existe valor maior, os dois são iguais.')