print('\033[7mPREÇO\033[m')


precoProduto = float(input('Informe o preço do produto -> R$'))


print('\033[4mFormas de pagamento\033[m:\n'
      '\033[1mDinheiro/Cheque\033[m\n'
      '[1] - À vista(10% de desconto) \n'
      '\033[1mCartão\033[m\n'
      '[2] - À vista(5% de desconto) \n'
      '[3] - 2x(sem juros)\n'
      '[4] - 3x ou mais(com juros)')


formaPagamento = int(input('Informe a opção de pagamento -> '))


if formaPagamento == 1:
    desconto = (precoProduto*10)/100
    precoDesconto = precoProduto - desconto
    print('Valor total -> R${:.2f}'.format(precoDesconto))


elif formaPagamento == 2:
    desconto = (precoProduto*5)/100
    precoDesconto = precoProduto - desconto
    print('Valor total -> R${:.2f}'.format(precoDesconto))


elif formaPagamento == 3:
    precoMensal = precoProduto/2
    print('Parcelas -> R${:.2f}'.format(precoMensal))


elif formaPagamento == 4:
    meses = int(input('Informe a quantidade de meses -> '))
    if meses > 2:
        juros = (precoProduto*20)/100
        precoJuros = precoProduto + juros
        precoMensal = precoJuros/meses
        print('Valor total com juros -> R${:.2f}\n'
              'Parcelas -> R${:.2f}'.format(precoJuros, precoMensal))
    else:
        print('Opção inválida!')


else:
    print('Opção inválida!')