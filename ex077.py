palavras = ('estudar','python','persoverar','foco','curso','gratis')
for p in palavras:
    print(f'\nNa palavra {p.upper()} tem as vogáis: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
