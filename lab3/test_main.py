import main

class TestBanco():
    def test_saida_correta_banco1(self):
        array_tempo_chegada = [0, 0, 1, 2, 30]
        array_duracao_atendimento = [5, 10, 10, 10, 10]
        assert(main.banco(1, array_tempo_chegada, array_duracao_atendimento) == 1)

    def test_saida_correta_banco2(self):
        array_tempo_chegada = [0, 0, 0, 3, 5, 7, 11, 13, 14, 15, 16, 17, 18, 19, 20, 23]
        array_duracao_atendimento = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 3, 10, 10, 3]
        assert(main.banco(3, array_tempo_chegada, array_duracao_atendimento) == 2)
