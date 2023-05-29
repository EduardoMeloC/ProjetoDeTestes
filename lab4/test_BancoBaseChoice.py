import Banco

class TestBancoBaseChoice():
    def test_saida_correta_banco_base(self):
        array_tempo_chegada = [1,2,3]
        array_duracao_atendimento = [1,5,10]
        assert(Banco.banco(2, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco1(self):
        array_tempo_chegada = [1,2,3]
        array_duracao_atendimento = [1,5,10]
        assert(Banco.banco(1, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco2(self):
        array_tempo_chegada = [1,2,3,4,5,6,7,8,9,10,11]
        array_duracao_atendimento = [5,5,5,5,5,5,5,5,5,5,5]
        assert(Banco.banco(10, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco5(self):
        array_tempo_chegada = [1,2]
        array_duracao_atendimento = [1,10]
        assert(Banco.banco(3, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco6(self):
        array_tempo_chegada = [1,2,3]
        array_duracao_atendimento = [1,5,10]
        assert(Banco.banco(3, array_tempo_chegada, array_duracao_atendimento) == 0)

    def test_saida_correta_banco7(self):
        array_tempo_chegada = [3,3,3]
        array_duracao_atendimento = [1,5,10]
        assert(Banco.banco(2, array_tempo_chegada, array_duracao_atendimento) == 0)
    
    def test_saida_correta_banco8(self):
        array_tempo_chegada = [1,2,3]
        array_duracao_atendimento = [10,10,10]
        assert(Banco.banco(3, array_tempo_chegada, array_duracao_atendimento) == 0)