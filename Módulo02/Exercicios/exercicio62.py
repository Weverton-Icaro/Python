'''Melhore o desafio 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar
0 termos.'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
N = 1
total = 0
mais = 10
while mais  != 0:
  total = total + mais
  while N <= total:
    print('{} '.format(termo), end='-> ')
    N+= 1
    termo += razão
  print('FIM')
  mais = int(input(' Deseja mostrar mais alguns termos ? '))
print('FIM')
print('Foram mostrados {} termos.'.format(total))
