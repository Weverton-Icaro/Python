#Calcule a soma entre todos os números impares
#que são multiplos de três a que se encontram
#no intervalo de 1 até 500

s = 0
for c in range (3, 500, 3):
  print(c)
  s += c
print('A soma dos multiplos de 3 à 500 é {}'.format(s))