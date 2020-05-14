c = 0
while c < 11:
  print(c)
  c += 2
print('FIM')

print('----------------------------------')

r = 'S'
while r == 'S':
  n = int(input('Digite um valor: '))
  r = str(input('Deseja digitar outro valor ? [S/N] : ')).upper()
print('FIM')

print('-------------------------------------')

num = 1
par = impar = 0
while num != 0 :
  num = int(input('Digite um valor: '))
  if num != 0:
    if num % 2 == 0:
      par += 1
    else:
      impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))
print('Acabou')
