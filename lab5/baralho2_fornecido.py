def baralho2(entrada):
    cartas = {'C': [], 'E': [], 'U': [], 'P': []}
    for i in range(0, len(entrada), 3):
        chave = entrada[i+2]
        cartas[chave] = cartas[chave] + [int(entrada[i:i+2])]

    faltam = {'C': 13, 'E': 13, 'U': 13, 'P': 13}
    for naipe in ['C', 'E', 'U', 'P']:
        for valor in range(1, 13):
            qtd = cartas[naipe].count(valor)
            if qtd > 1:
                faltam[naipe] = 'erro'
            elif qtd == 1 and faltam[naipe] != 'erro':
                faltam[naipe] -= 1
    return [faltam['C'], faltam['E'], faltam['U'], faltam['P']]
