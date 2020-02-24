#Faça um programa que leia um número de 0 a 9999
# emostre na tela cada um dos digitos separados.

#Ex.: Digite um número : 1834
# unidade: 4
# dezenas: 3
# centena: 8
# milha: 1

num = input('Digite um numéro de 0 a 9999: ')
print('Unidade:{}'.format(num[3]))
print('Dezena:{}'.format(num[2]))
print('Centena:{}'.format(num[1]))
print('Milhar:{}'.format(num[0]))
