#Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 O nome com todas as letras maiusculas
# 2 O nome com todas minusculas
# 3 Quantas letras ao tod.o ( sem considerar espaços)
# 4 Quantas letras tem o primeiro nome.

frase = str(input('Escreva seu nome completo: ')).strip()
print(frase)
print('Seu nome com letras maiusculas é :{}'.format(frase.upper()))
print('Seu nome com letras minusculas é :{}'.format(frase.lower()))
print('Seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))
dividido = frase.split()
print('Seu primeiro nome tem {} letras.'.format(len(dividido[0]) - dividido.count(' ')))

