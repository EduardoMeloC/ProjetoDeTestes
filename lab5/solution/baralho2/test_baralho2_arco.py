import baralho2


class TestBaralho1Arco():
    def test_baralho_1(self):
        input_str = "11C12P12P"
        assert (baralho2.baralho2(input_str) == [12, 13, 13, 'erro'])
