#Desenvolver um programa que leia
# 6 números inteiros e mostre a soma apenas daqueles que forem pares
#Se o valor digitado for Impar, desconsidere-o.

cont = 0
soma=0
for c in range (1, 7):
  num = int(input('Digite o {} valor: '.format(c)))
  if num % 2 == 0:
    soma += num
    cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))