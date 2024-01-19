import unittest
from resta import restar

class TestRestar(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-5, -3), -2)
        self.assertEqual(restar(-5, 3), -8)
        self.assertEqual(restar(5, 0), 5)

if __name__ == '__main__':
    unittest.main()     