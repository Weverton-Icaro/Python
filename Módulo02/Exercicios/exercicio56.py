#Leia o nome, idade e sexo de 4 pessoas
#Mostre a media de idade do grupo
#Qual o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaidade = 0
mediaidade = 0
nomevelho = ''
idadehomem = 0
idademulher = 0
nomemulher = ''
for pessoa in range (1, 5):
  print('-----------------------------------------')
  nome = str(input('Informe o nome da {}ª pessoa: '.format(pessoa))).strip()
  idade = int(input('Informe o a idade da {}ª pessoa: '.format(pessoa)))
  sexo = str(input('Informe o sexo da {}ª pessoa, M/F: '.format(pessoa))).strip().upper()
  somaidade += idade

  if pessoa == 1 and sexo in 'M' :
    idadehomem = idade
    nomevelho = nome

  if sexo in 'M' and idade > idadehomem :
    idadehomem = idade
    nomevelho = nome

  if sexo in 'F' and idade < 20 :
    idademulher += 1
    if idademulher == 1:
      nomemulher = nome

print('-----------------------------------------')
mediaidade = somaidade / 4
print('A média das idades é {}. '.format(mediaidade))

print('-----------------------------------------')
print('O homem mais velho é {} e tem {} anos.'.format(nomevelho, idadehomem))

print('-----------------------------------------')
print('{} mulher(s) tem menos de 20 anos. {} '.format(idademulher, nomemulher))