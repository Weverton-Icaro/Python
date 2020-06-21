'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma
PA, mostrando os 10 primeiros termos da progressão usando a estrutura While.'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
N = 1
while N <= 10 :
    print('{} '.format(termo), end='-> ')
    N+= 1
    termo += razão
print('Fim')