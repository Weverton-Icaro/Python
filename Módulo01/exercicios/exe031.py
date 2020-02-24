km = int(input('Qual será a distância percorrida em Km? '))
km1 = (km * 0.45)
km2 = (km * 0.50)
if km >=200 :
    print('O valor da passagem será R${:2}, pois passa de 200Km'.format(km1))
else:
    print('O valor da passagem será R${:2}, pois não passa de 200Km. '.format(km2))

print('--FIM--')