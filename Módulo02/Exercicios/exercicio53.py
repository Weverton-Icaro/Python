#Crie um programa que leia uma frase e diga se ela é palindromo
#desconsiderando os espaços.
#Ex:
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#MARATONA
#ANOTARAM A DATA DA

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()

junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = ''
for letra in range (len(junto) -1, -1, -1):
  inverso += junto[letra]'''
if inverso == junto :
  print('Temos uma frase palindroma: {}, {}'.format(junto, inverso))
else :
  print('A frase {}, não é palindroma.'.format(frase))