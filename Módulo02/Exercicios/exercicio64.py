'''
Crie um programa que leia varios numeros inteiros pelo teclado.
O programa vai parar quando o usuário digitar o valor 999, que é a condição de
parada. No final, mostre quantos numeros foram digitados e qual foi a soma
entre eles. (desconsiderando o flag)
'''

num = 0
cont = 0
total = cont
c = 0
while num != 999:
  num = int(input('Digite um número: '))
  cont += num
  total =+ cont
  c += 1
print('A soma dos valores é {}, foram somados {} números.'.format(total, c))
print('FIM')
