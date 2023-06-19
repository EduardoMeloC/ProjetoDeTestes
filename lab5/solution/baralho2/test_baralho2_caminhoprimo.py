import baralho2


class TestBaralhoCaminhoPrimo():
    def test_baralho_1(self):
        input_str = ""
        assert (baralho2.baralho2(input_str) == [13, 13, 13, 13])

    def test_baralho_2(self):
        input_str = "01C13C01E02E03E03E04E04E06E06E01U01U13U13U13P"
        assert (baralho2.baralho2(input_str) == [11, 'erro', 'erro', 12])

    def test_baralho_3(self):
        input_str = "01C 01C 13P 13P"
        assert (baralho2.baralho2(input_str) == ['erro', 13, 13, 'erro'])

    def test_baralho_4(self):
        input_str = "05E"
        assert (baralho2.baralho2(input_str) == [13, 12, 13, 13])
