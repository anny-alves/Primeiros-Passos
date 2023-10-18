print('====== SIMULADOR DE LOJA ======')
valor = float(input('Informe o valor da sua compra: '))
print('FORMA DE PAGAMENTO')
print('''[ 1 ] à vista dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
fp = int(input('Informe a opção de pagamento: '))
if fp == 4:
    p = int(input('Informe o número de parcelas: '))
    pf = valor + valor*0.2
    vp = pf / p
    print('Sua compra de R${:.2f} parcelada em {}x no cartão com o juros ficará R${:.2f}'.format(valor, p, pf ))
    print('Voce pagará em {}x de R${:.2f}'.format(p, vp))
elif fp == 1:
    pf = valor - valor*0.1
    print('Pagando à vista o valor de sua compra passa a ser R${:.2f}'.format(pf))
elif fp == 2:
    pf = valor - valor*0.05
    print('Pagando à vista no cartão sua compra sai por R${:.2f}'.format(pf))
elif fp == 3:
    vp = valor / 2
    print('Nessa forma de pagamento o valor permanece o mesmo e \n será pago em 2x de R${:.2f}'. format(vp))
else:
    print('Opção inválida, tente novamente.')
