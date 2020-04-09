idade = int(input('Informe a idade: '))

if(idade <= 9):
  print('Mirim')
elif(idade >= 10 and idade <=14):
  print('Infantil')
elif(idade >=15 and idade <19):
  print('Junior')
elif(idade >= 19 and idade <=20):
  print('Senior')
else:
  print('Master')