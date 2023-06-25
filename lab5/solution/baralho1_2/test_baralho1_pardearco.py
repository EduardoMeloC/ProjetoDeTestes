import baralho1


class TestBaralho1ParDeArco():
    def test_baralho_1(self):
        input_str = "11C12P12P"
        assert (baralho1.baralho1(input_str) == [12, 13, 13, 'erro'])

    def test_baralho_2(self):
        input_str = ""
        assert (baralho1.baralho1(input_str) == [13, 13, 13, 13])
