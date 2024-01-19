import unittest
from division import dividir

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-6, -2), 3)
        self.assertEqual(dividir(-6, 2), -3)

    def test_dividir_por_uno(self):
        self.assertEqual(dividir(5, 1), 5)
        self.assertEqual(dividir(-3, 1), -3)

    def test_dividir_valores_limite(self):
        self.assertEqual(dividir(float('inf'), 2), float('inf'))
        self.assertEqual(dividir(float('-inf'), -2), float('inf'))

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()