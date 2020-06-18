'''Faça um programa que leia um número qualquer e mostre o seu FATORIAL

ex.: 5! = 5x4x3x2x1=120'''
from math import factorial

num = int(input('Digite um número: '))
fact = factorial(num)
n = num
while n > 0 :
  print('{}'.format(n), end='')
  print(' x ' if n > 1 else ' = {}'.format(fact), end='')
  n -= 1
print('O fatorial de {} é {}.'.format(num, fact))