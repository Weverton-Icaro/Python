'''Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.

ex.: 0 -> 1 -> 2 -> 3 -> 5 -> 8 ...'''

rep = int(input('Informe quantos números da seguência de Fibonacci deseja visualizar: '))

n1 = 0
n2 = 1
print('{} -> {} -> '.format(n1, n2), end='')
contador = 3
while contador <= rep:
  n3 = n1 + n2
  print('{} -> '.format(n3), end='')
  n1 = n2
  n2 = n3
  contador += 1
print('FIM')