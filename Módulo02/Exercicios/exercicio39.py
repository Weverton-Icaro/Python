ano = int(input('Informe o ano de nascimento: '))
idade = (2020 - ano)
print('Você tem {} anos de idade.'.format(idade))

if(idade < 18):
  print('Você ainda vai se alistar ao serviço militar!')
  falta = (idade - 18)
  print('Faltam {} anos para se alistar.'.format(falta))
elif(idade == 18):
  print('Você tem {} anos, já está na hora de se alistar.'.format(idade))
else:
  passou = (idade - 18)
  print('Você está com {} anos, já passou do periodo de se alistar à {} anos.'.format(idade, passou))
