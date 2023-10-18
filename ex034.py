print('====== Cheque o seu aumento aqui ======')
s = float(input('Qual o valor do seu salário atual: '))
if s > 1250:
    a = '10%'
    ns = s + (s * 0.10)
else:
    a = '15%'
    ns = s + ( s * 0.15)
print('Para o salário antigo de R${:.2f} seu aumento é de {}. \n Seu novo salário será R${:.2f}'.format(s, a, ns))
