#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o ultimo nome separadamente

nome = input('Digite seu nome completo: ')

print(nome)
dividido = nome.split()
print(dividido[0])
print(dividido[-1])
