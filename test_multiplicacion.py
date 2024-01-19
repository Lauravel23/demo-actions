import unittest
from multiplicacion import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(-2, -3), 6)
        self.assertEqual(multiplicar(-2, 3), -6)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(0, -3), 0)

    def test_multiplicar_por_uno(self):
        self.assertEqual(multiplicar(5, 1), 5)
        self.assertEqual(multiplicar(-3, 1), -3)

    def test_multiplicar_valores_limite(self):
        self.assertEqual(multiplicar(float('inf'), 2), float('inf'))
        self.assertEqual(multiplicar(float('-inf'), -2), float('inf'))

if __name__ == '__main__':
    unittest.main()