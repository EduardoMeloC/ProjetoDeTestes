import Banco

class TestBancoPairwise():
    def test_saida_correta_banco1(self):
        array_tempo_chegada = [0]
        array_duracao_atendimento = [10]
        assert(Banco.banco(1, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco2(self):
        array_tempo_chegada = [2, 2, 2, 6]
        array_duracao_atendimento = [5, 6, 2, 10]
        assert(Banco.banco(1, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco3(self):
        array_tempo_chegada = 1000*[0]
        array_duracao_atendimento = 1000*[10]
        assert(Banco.banco(1, array_tempo_chegada, array_duracao_atendimento) == 997)

    def test_saida_correta_banco4(self):
        array_tempo_chegada = [0]
        array_duracao_atendimento = [10]
        assert(Banco.banco(4, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco5(self):
        array_tempo_chegada = [2,2,2,6]
        array_duracao_atendimento = [5,6,2,10]
        assert(Banco.banco(4, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco6(self):
        array_tempo_chegada = 1000*[0]
        array_duracao_atendimento = 1000*[10]
        assert(Banco.banco(4, array_tempo_chegada, array_duracao_atendimento) == 988)

    def test_saida_correta_banco7(self):
        array_tempo_chegada = [0]
        array_duracao_atendimento = [10]
        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco8(self):
        array_tempo_chegada = [2,2,2,6]
        array_duracao_atendimento = [5,6,2,10]
        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco9(self):
        array_tempo_chegada = 1000*[0]
        array_duracao_atendimento = 1000*[10]
        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 970)

    def test_saida_correta_banco10(self):
        array_tempo_chegada = 10*[0]
        array_duracao_atendimento = 10*[10]
        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco11(self):
        array_tempo_chegada = [1,2,3,4]
        array_duracao_atendimento = 4*[10]
        assert(Banco.banco(4, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco12(self):
        array_tempo_chegada = [1,2,3,4]
        array_duracao_atendimento = [5,6,2,10]
        assert(Banco.banco(4, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco13(self):
        array_tempo_chegada = [0]
        array_duracao_atendimento = [1]
        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco14(self):
        array_tempo_chegada = 1000*[0]
        array_duracao_atendimento = 1000*[5]
        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 950)

    def test_saida_correta_banco15(self):
        array_tempo_chegada = [1,2,3,4,5]
        array_duracao_atendimento = [5,6,2,10,1]
        assert(Banco.banco(4, array_tempo_chegada, array_duracao_atendimento) == 0)