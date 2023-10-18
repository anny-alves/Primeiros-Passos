from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento (aaaa): '))
anoa = date.today()
dados['Idade'] = anoa.year - nasc
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação (aaaa): '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Contratação'] - nasc) + 35
print(dados)
print('-='*20)
for k, v in dados.items():
    print(f'{k}: {v}')
