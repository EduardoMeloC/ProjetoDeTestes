import Banco

def test_saida_correta_banco3():
    array_tempo_chegada = [0, 0, 0]
    array_duracao_atendimento = [20, 20, 20]
    out = Banco.banco(1, array_tempo_chegada, array_duracao_atendimento)
    assert(out == 1)
    print(out)

test_saida_correta_banco3()