from unittest import TestCase
import sys
sys.path.append("..")
from triangulo1 import TrianguloDefeituoso1

equilatero = "equilatero"
isosceles = "isosceles"
escaleno = "escaleno"
invalido = "invalido"

class TrianguloTest(TestCase):

    def test_triangulo(self):
        for caso_teste in self.todos_testes:
            self.assertEqual(TrianguloDefeituoso1.TipoTriangulo(*caso_teste["entrada"]), caso_teste["saida"])
    
    testes_de_aula = [
    { "entrada": [1, 1, 1], "saida": equilatero },
    { "entrada": [1, 1, 2], "saida": invalido },
    { "entrada": [3, 3, 2], "saida": isosceles },
    { "entrada": [2, 3, 3], "saida": isosceles },
    { "entrada": [3, 2, 3], "saida": isosceles },
    { "entrada": [2, 4, 5], "saida": escaleno },
    { "entrada": [4, 2, 5], "saida": escaleno },
    { "entrada": [5, 2, 4], "saida": escaleno },
    { "entrada": [5, 4, 2], "saida": escaleno },
    { "entrada": [2, 5, 4], "saida": escaleno },
    { "entrada": [4, 5, 2], "saida": escaleno },
    { "entrada": [0, 1, 2], "saida": invalido },
    { "entrada": [-2, 4, 5], "saida": invalido },
    ]
        
    testes_que_faltam = [
    { "entrada": [1, 2, 1], "saida": invalido },
    { "entrada": [2, 1, 1], "saida": invalido },
    { "entrada": [2, 3, 9], "saida": invalido },
    { "entrada": [2, 9, 3], "saida": invalido },
    { "entrada": [3, 9, 2], "saida": invalido },
    { "entrada": [9, 2, 3], "saida": invalido },
    { "entrada": [9, 3, 2], "saida": invalido },
    { "entrada": [0, 0, 0], "saida": invalido },
    { "entrada": [2.5, 3.5, 5.5], "saida": escaleno },
    # { "entrada": [2, 1], "saida": invalido }, # Removido porque lança um TypeError
    ]

    todos_testes = [*testes_de_aula, *testes_que_faltam]

    
