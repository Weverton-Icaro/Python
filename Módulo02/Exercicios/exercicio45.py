from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Qual é a sua jogada?'))
print('--'*12)
print('Compuador jogou --> {}'.format(itens[computador]))
print('Jogador jogou --> {}'.format(itens[jogador]))
print('--'*12)
if(jogador == 0 and computador == 2):
  print('O ganhador foi --> Jogador')
elif(jogador == 0 and computador == 1):
  print('O ganhador foi --> Computador')
elif(jogador == 0 and computaodor == 0):
  print('Deu empate.')
elif(jogador == 1 and computador == 0):
  print('O ganhador foi --> Jogador')
elif(jogador == 1 and computador == 2):
  print('O ganhador foi --> Computador')
elif(jogador == 1 and computaodor == 1):
  print('Deu empate.')
elif(jogador == 2 and computador == 1):
  print('O ganhador foi --> Jogador')
elif(jogador == 2 and computador == 0):
  print('O ganhador foi --> Computador')
elif(jogador == 2 and computaodor == 2):
  print('Deu empate.')