# Faça um programa que crie uma contagem para estouro de fogos
#contando de 10 até 0 com pausa de 1 segundo.
from time import sleep

print('Estouro de fogos em ')
for c in range(10, 0, -1):
  sleep(1.0)
  print(c)
print('FIM ')