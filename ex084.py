galera = list()
dados = list()
op = ' '
p = 0
leves = list()
pesados = list()
maior = 0
menor = 0
while op not in 'Nn':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    galera.append(dados[:])
    dados.clear()
    p += 1
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
for pos, c in enumerate(galera):
    if pos == 0:
        maior = galera[0][1]
        menor = galera[0][1]
        pesados.append(galera[0][0])
        leves.append(galera[0][0])
    else:
        if maior == galera[pos][1]:
            pesados.append(galera[pos][0])
        elif maior > galera[pos][1]:
            pesados.clear()
            maior = galera[pos][1]
            pesados.append(galera[pos][0])
        elif menor == galera[pos][1]:
            leves.append(galera[pos][0])
        elif menor < galera[pos][1]:
            leves.clear()
            menor = galera[pos][1]
            leves.append(galera[pos][0])
print(f'Foram cadastradas {p} pessoas. São elas {galera}')
print(f'O maior peso foi {maior}Kg que foi o peso de {pesados}')
print(f'O menor peso foi {menor}Kg que foi o peso de {leves}')
