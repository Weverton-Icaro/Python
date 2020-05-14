#Leia o ano de nascimento de 7 pessoas
#No final mostre quantas pessoas ainda não atingiram a maior idade
#e quantos já são maiores.

from datetime import date
atual = date.today().year
pessmaior = 0
pessmenor = 0
for pessoa in range (1, 8):
  nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
  idade = atual - nasc
  if idade >= 21:
    pessmaior += 1
    print('Essa pessoa é maior de idade.')
  else:
    pessmenor += 1
    print('Essa pessoa é menor de idade.')

print('Ao todo tivemos {} pessoas maiores de idade e {} menores de idade.'.format(pessmaior, pessmenor))
