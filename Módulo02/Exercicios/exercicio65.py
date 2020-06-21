'''
Crie um programa que leia varios numeros inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valor lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.
'''

r = 'S'
soma = cont = media = menor = maior = c = 0
while r == 'S':
  num = int(input('Digite um número: '))
  soma += num
  cont += 1
  c += 1
  r = str(input('Deseja digitar mais números? [S/N]')).upper().strip()[0]
  if cont == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
media = soma / cont
print('''A média entre os valores é {},
O menor número foi {},
O maior número foi {},
foram informados {} valores.'''.format(media, menor, maior, c))
print('FIM')