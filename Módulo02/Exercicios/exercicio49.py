# Faça uma tabuada utilizando o laço FOR

num = int(input('Digite o valor para gerar a tabuada: '))
s = 0
for c in range (0, 10, 1):
  print('{} x {:2} = {}'.format(num, c+1, num*(c+1)))
print('FIM')