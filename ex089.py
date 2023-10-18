op = ' '
lista = list()
dados = list()
while op not in 'Nn':
    nome = str(input('Nome: '))
    dados.append(nome)
    nota1 = float(input('1° Nota: '))
    dados.append(nota1)
    nota2 = float(input('2° Nota: '))
    dados.append(nota2)
    med = (nota1 + nota2)/2
    dados.append(med)
    lista.append(dados[:])
    dados.clear()
    op = str(input('Deseja incluir mais um aluno?: [S/N]'))
print('='*15)
print(f'No. Nome{" ":5} Média')
for pos, c in enumerate(lista):
    print(f'{pos:<4}{lista[pos][0]:<10}{lista[pos][3]:>8.1f}')
print('='*15)
resp = 0
#com essa condição não está havendo parada
while resp not in 999:
    resp = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    print(f' As notas do aluno {lista[resp][0]} na primeira avaliação {lista[resp][1]} e na segunda avaliação {lista[resp][2]}')
