1. Usar o grafo fornecido para o projeto de testes baseado em grafos. Projetar separadamente usando critério de cobertura de nós, arcos, pares de arcos e caminhos primos. Pode usar a ferramenta do site do livro para a geração dos caminhos primos. Não usem para a definição dos casos de teste.

Sugestão para o projeto dos casos de teste concretos: definam o valor de entrada primeiro, usando como referência os requisitos e DEPOIS, verifiquem que requisitos foram satisfeitos.

2. Criar os scripts de teste para cada um dos projetos separadamente

3. Por último, avaliem os conjuntos de teste obtidos usando mutação no código original e no código adicional fornecido aqui.

![grafo fornecido](./grafo.jpeg)

```python
def baralho1(entrada):

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
    while valor != '14':
        while i < len(cartas) and cartas[i][:2] == valor:
            naipe = cartas[i][2]
            if naipe == 'C':
                copas = copas - 1
            elif naipe == 'E':
                espadas = espadas - 1
            elif naipe == 'P':
                paus = paus - 1
            else:
                ouros = ouros - 1
            i = i + 1
        valor = str(int(valor) + 1)
        if len(valor) == 1:
            valor = '0' + valor
    return [copas, espadas, ouros, paus]

def main():
    entrada = input()
    resultado =   baralho1(entrada)
    print (resultado[0])
    print (resultado[1])
    print (resultado[2])
    print (resultado[3])

main()
```

```python
def baralho2(entrada):

    cartas = {'C':[], 'E':[],'U':[],'P':[]}
    for i in range(0,len(entrada),3):
        chave = entrada[i+2]
        cartas[chave] = cartas[chave] + [int(entrada[i:i+2])]

    faltam = {'C':13,'E':13,'U':13,'P':13}
    for naipe in ['C','E','U','P']:
        for valor in range(1,13):
            qtd = cartas[naipe].count(valor)
            if qtd > 1:
                faltam[naipe] = 'erro'
            elif qtd == 1 and faltam[naipe] != 'erro':
                faltam[naipe] -= 1
    return [faltam['C'], faltam['E'], faltam['U'], faltam['P']]


def main():
    entrada = input()
    resultado =   baralho2(entrada)
    print (resultado[0])
    print (resultado[1])
    print (resultado[2])
    print (resultado[3])

main()
```
