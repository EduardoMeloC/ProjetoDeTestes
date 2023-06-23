def baralho1(entrada):
    #return baralho1_2(entrada)
    return baralho1_1(entrada)

def baralho1_1(entrada):

    cartas = []
    for i in range(0,len(entrada),3):
        cartas = cartas + [entrada[i:i+3]]

    cartas.sort()
    #print(cartas)
    
    copas = 13
    espadas = 13
    ouros = 13
    paus = 13

    valor = '01'
    i = 0
    ultima = '00A'
    while valor != '14':       
        while i < len(cartas) and cartas[i][:2] == valor:
            naipe = cartas[i][2]
            
            if naipe == 'C' and copas != 'erro':
                copas = 'erro' if cartas[i] == ultima else copas - 1
            elif naipe == 'E' and espadas != 'erro':
                espadas = 'erro' if cartas[i] == ultima else espadas - 1
            elif naipe == 'P' and paus != 'erro':
                paus = 'erro' if cartas[i] == ultima else paus - 1
            elif naipe == 'U' and ouros != 'erro':
                ouros = 'erro' if cartas[i] == ultima else ouros - 1
            
            ultima = cartas[i]
            i = i + 1
        valor = str(int(valor) + 1)
        if len(valor) == 1:
            valor = '0' + valor
    return [copas, espadas, ouros, paus]

def baralho1_2(entrada):

    cartas = []
    for i in range(0, len(entrada), 3):
        cartas = cartas + [entrada[i:i+3]]

    cartas.sort()
    # print(cartas)

    nCartas={
        "C": 13,
        "E": 13,
        "U": 13,
        "P": 13
    }

    valor = '01'
    i = 0
    while valor != '14':
        while i < len(cartas) and cartas[i][:2] == valor:
            naipe = cartas[i][2]

            if (i-1 >= 0 and cartas[i] == cartas[i-1] or
                nCartas[naipe] == 'erro'):
                nCartas[naipe] = 'erro'
            else:
                nCartas[naipe] = nCartas[naipe] - 1
            
            i = i + 1
        valor = str(int(valor) + 1)
        if len(valor) == 1:
            valor = '0' + valor
    return list(nCartas.values())