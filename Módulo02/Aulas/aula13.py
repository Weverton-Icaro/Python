for c in range(0,20, 2):
  print(c)
print('FIM')
print('______________________________________________')

n = int(input('Digite um numero:'))
for c in range(0, n):
  print(c)
print('Fim')
print('______________________________________________')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
  print(c)
print('Fim')
print('______________________________________________')

soma = 0
for c in range(0,4):
  print(int(input('Digite um valor: ')))
  soma += n
print('O somatório dos valores é {}'.format(soma))