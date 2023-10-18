print('===== CALCULE SUA PASSAGEM AQUI =====')
dist = float(input('Insira a distânci d sua viagem em quuilomêtros: '))
if dist <= 200:
    p = dist * 0.5
    print('Para uma distância de {:.2f}km o valor da sua passagem custará {} reais.'.format(dist, p))
else:
    p = dist * 0.45
    print('Para uma distância de {:.2f}km o valor da sua passagem custará {} reais.'.format(dist, p))
