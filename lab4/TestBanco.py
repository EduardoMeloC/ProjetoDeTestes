import Banco

class TestBanco():
    def test_saida_correta_banco1(self):
        array_tempo_chegada = [0]
        array_duracao_atendimento = [10]
        assert(Banco.banco(1, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco2(self):
        array_tempo_chegada = [2, 2, 2, 6]
        array_duracao_atendimento = [5, 6, 2, 10]
        assert(Banco.banco(9, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco3(self):
        array_tempo_chegada = []
        array_duracao_atendimento = []
        for i in range(1000):
            array_tempo_chegada.append(0)
            array_duracao_atendimento.append(10)

        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 970)
