# Author:
#   Henrique Trivelato de Angelo

from calcula import calculadora

class TestClass:

    # Testando +
    def test_one(self):
        elemento_1 = 1
        elemento_2 = 2
        operation = "+"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == 3

    # Testando -
    def test_two(self):
        elemento_1 = 1
        elemento_2 = 2
        operation = "-"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == -1

    # Testando *
    def test_three(self):
        elemento_1 = 1
        elemento_2 = 2
        operation = "*"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == 2

    # Testando /
    def test_four(self):
        elemento_1 = 1
        elemento_2 = 2
        operation = "/"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == 0.5

    # Testando ^
    def test_five(self):
        elemento_1 = 1
        elemento_2 = 2
        operation = "^"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == 1

    # Testando número negativo
    def test_six(self):
        elemento_1 = -10
        elemento_2 = 2
        operation = "+"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == -8

    # Testando número decimal
    def test_seven(self):
        elemento_1 = 23.75
        elemento_2 = 1.25
        operation = "-"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == 22.5

    # Testando número decimal e negativo
    def test_eight(self):
        elemento_1 = -23.75
        elemento_2 = 3
        operation = "*"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == -71.25

    # Testando divisão por 0
    def test_nine(self):
        elemento_1 = 75
        elemento_2 = 0
        operation = "/"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

        # Testando elemento 1 inválido
    def test_ten(self):
        elemento_1 = "a"
        elemento_2 = 5.6
        operation = "-"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

    # Testando elemento 2 inválido
    def test_eleven(self):
        elemento_1 = 3.7
        elemento_2 = "b"
        operation = "+"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

    # Testando sinal inválido
    def test_twelve(self):
        elemento_1 = 75
        elemento_2 = 1
        operation = "#"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

    # Testando 2 elementos inválidos
    def test_thirteen(self):
        elemento_1 = "-23.4.5"
        elemento_2 = "b"
        operation = "+"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

    # Testando elemento 1 inválido e sinal inválido
    def test_fourteen(self):
        elemento_1 = "-23.4.5"
        elemento_2 = "2.3"
        operation = ")"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

    # Testando elemento 2 inválido e sinal inválido
    def test_fiftteen(self):
        elemento_1 = "-1.23"
        elemento_2 = "-."
        operation = "&"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

    # Testando as 3 entradas inválidas
    def test_sixteen(self):
        elemento_1 = "123.hue"
        elemento_2 = "-."
        operation = "&"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == None

    # Testando Exponenciação
    def test_seventeen(self):
        elemento_1 = -3
        elemento_2 = 4
        operation = "^"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == 81

    # Testando se resultado do produto de floats é diferente do de int
    def test_seventeen(self):
        elemento_1 = 5.0
        elemento_2 = 7.0
        operation = "*"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == (5*7)

    # Testando se resultado da divisão de floats é diferente da de int
    def test_eighteen(self):
        elemento_1 = 15.0
        elemento_2 = 5.0
        operation = "/"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == (15/5)

    # Testando soma de negativo com posititvo
    def test_nineteen(self):
        elemento_1 = 7.5
        elemento_2 = -8.25
        operation = "+"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == -0.75

    # Testando subtração de negativo com posititvo
    def test_twenty(self):
        elemento_1 = -7.5
        elemento_2 = 23
        operation = "-"
        resultado = calculadora(elemento_1, elemento_2, operation)
        assert resultado == -30.5