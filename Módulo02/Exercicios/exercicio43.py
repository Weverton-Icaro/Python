altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))
imc = peso / altura
print('Seu IMC é {:.2f}.'.format(imc))

if(imc <= 18.5):
  print('Abaixo do peso')
elif(imc >= 18.5 and imc <= 25):
  print('Peso Ideal')
elif(imc > 25 and imc <= 30):
  print('Sobrepeso')
elif(imc > 30 and imc <=40):
  print('Obesidade')
else:
  print('Obesidade mórbida')