def baralho1(entrada):

    cartas = []
    for i in range(0, len(entrada), 3):
        cartas = cartas + [entrada[i:i+3]]

    cartas.sort()
    # print(cartas)

    nCartas = {
        "C": 13,
        "E": 13,
        "U": 13,
        "P": 13
    }

    valor = '01'
    i = 0
    while valor != '14':  # pragma: no mutate
        while i < len(cartas) and cartas[i][:2] == valor:
            naipe = cartas[i][2]

            if (i-1 >= 0 and cartas[i] == cartas[i-1] or
                    nCartas[naipe] == 'erro'):
                nCartas[naipe] = 'erro'
            else:
                nCartas[naipe] = nCartas[naipe] - 1

            i = i + 1
        valor = str(int(valor) + 1)  # pragma: no mutate
        if len(valor) == 1:  # pragma: no mutate
            valor = '0' + valor
    return list(nCartas.values())
