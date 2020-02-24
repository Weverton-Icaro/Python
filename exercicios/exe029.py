# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar a velocidade de 80Km/h, mostre a mnsagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

vel = int(input('Qual a velocidade do carro? '))
if vel >=80:
   print('Você foi multado em R${} por ultrapassar o limite de velocidade'.format((vel - 80) * 7))

else:
    print('Mantenha-se abaixo do limite.')
