maiores = m20 = man = 0
while True:
    print('-'*30)
    print(f'{"CADASTRO DE PESSOAS":^30}')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        man +=1
    if idade >= 18:
        maiores += 1
    elif sexo == 'F' and idade <= 20:
        m20 += 1
    print('-'*30)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    print('-'*30)
    if opc == 'N':
        break
print(f'''o Total de pessoas com maior de 18 anos foi: {maiores} \n
Ao todo temos {man} homens cadastrados \n
E temos {m20} mulheres com menos de 20 anos''')
