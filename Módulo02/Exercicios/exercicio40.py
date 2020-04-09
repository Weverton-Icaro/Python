nota1 = float(input('infome a primeira nota: '))
nota2 = float(input('informe a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))

if(media >= 7):
  print('Aprovado, sua média foi {:.1f}'.format(media))
elif(media >=5.1 and media <=6.9):
  print('O aluno está de recuperação, sua média foi {:.1f}'.format(media))
else:
  print('Reprovado, sua média foi {:.1f}'.format(media))