import unittest
from resta import restar

class TestRestar(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-5, -3), -2)
        self.assertEqual(restar(-5, 3), -8)
        self.assertEqual(restar(5, 0), 5)

    def test_restar_valores_limite(self):
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(float('inf'), 1), float('inf'))
        self.assertEqual(restar(float('-inf'), -1), float('-inf'))

if __name__ == '__main__':
    unittest.main()     