nome = str(input('Qual é o seu nome? '))
if nome == 'Weverton':
  print('Que belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
  print('Seu nome é bem popular no Brasil.')
else:
  print('Seu nome é bem normal!')
print('Tenha um bom dia , {}!'.format(nome))