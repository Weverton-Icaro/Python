'''Melhore o jogo do Exercicio 028 onde o computador vai "pensar" em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''

from random import randint

computador = randint(0, 10)
nome = str(input('Infome seu nome: '))
print('Olá {}, pensei em um número, consegue adivinhar qual foi? '.format(nome))
tentativa = 0
acertou = False
while not acertou:
  jogador = int(input('Dê um palpite? '))
  tentativa += 1
  if jogador == computador :
    acertou = True
  else:
    if jogador < computador:
      print('Mais')
    else:
      print('Menos')
print('Parabéns {}, conseguiu na {}ª tentativa.'.format(nome, tentativa))
