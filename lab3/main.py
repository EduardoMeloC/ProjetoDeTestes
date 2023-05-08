def main():
    C, N = [int(x) for x in input().split()]
    T = []
    D = []
    for i in range(N):
        Ti, Di = [int(x) for x in input().split()]
        T.append(Ti)
        D.append(Di)
    print(banco(C, T, D))

def banco(C, T, D):
    n_clientes_tristes = 0
    clientes_sendo_atendidos = []
    fila_de_espera = []
    # contagem_de_espera = []
    for time in range(310):
        if len(fila_de_espera) > 0:
            for DiEi in fila_de_espera:
                DiEi[1] += 1
                if DiEi[1] == 20:
                    n_clientes_tristes += 1
            for _ in range(C - len(clientes_sendo_atendidos)):
                clientes_sendo_atendidos.append(fila_de_espera.pop(0)[0])
                if len(fila_de_espera) == 0:
                    break

        for Ti, Di in zip(T, D):
            if time == Ti:
                if len(clientes_sendo_atendidos) < C:
                    clientes_sendo_atendidos.append(Di)
                else:
                    fila_de_espera.append([Di, 0])
                    # contagem_de_espera.append(0)

        # @TODO: remove
        #for i, Ci in enumerate(contagem_de_espera):
        #    contagem_de_espera[i] += 1
        #    if contagem_de_espera[i] == 20:
        #        n_clientes_tristes += 1

        for i, Di in enumerate(clientes_sendo_atendidos):
            clientes_sendo_atendidos[i] -= 1
            if clientes_sendo_atendidos[i] == 0:
                clientes_sendo_atendidos.pop(i)

        #if(len(clientes_sendo_atendidos)!=0 or len(fila_de_espera)!=0):
        #print(f"time: {time+1}")
        #print(f"clientes_sendo_atendidos: {clientes_sendo_atendidos}")
        #print(f"fila_de_espera: {fila_de_espera}")
        #print(f"-")
    return n_clientes_tristes








main()
