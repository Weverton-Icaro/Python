#Leia o peso de 5 pessoas e mostre qual é o maior e o menor peso registrado

maior = 0
menor = 0
for pessoa in range (1, 6):
  peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
  if pessoa == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print('O maior peso é {}Kg.'.format(maior))
print('O menor peso é {}Kg.'.format(menor))
