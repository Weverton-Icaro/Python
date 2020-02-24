ano = int(input('Informe um ano e eu lhe direi se é bissexto: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano {ano} informado é bissexto.')
else:
    print(f'O ano {ano} informado não é bissexto.')