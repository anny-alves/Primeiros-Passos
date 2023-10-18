print('===== Radar de velocidade =====')
v = float(input('A que velocidade você estava? '))
if v <= 50:
    print("Parabéns, você estava andando a {:.1f}Km/h dentro do limíte de velocidade.")
else:
    m = (v - 80)*7
    print('Você estava fora do limite de velocidade,\n a {:.1f}Km/h sua multa é {:.1f} reais'.format(v, m))
