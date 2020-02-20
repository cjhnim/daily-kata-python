import unittest
from diamond import Diamond

class DiamondTests(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(1, 1)

    def test_A_has_A(self):
        d = Diamond('A')
        self.assertEqual("A\n", d.show())

    def test_B_has_ABBA(self):
        d = Diamond('B') 
        expected = \
                " A\n"+\
                "B B\n"+\
                " A\n"

        self.assertEqual(expected, d.show())

    def test_C_has_ABBCCA(self):
        d = Diamond('C')
        expected = \
                "  A\n"+\
                " B B\n"+\
                "C C\n"+\
                " B B\n"+\
                "  A\n"
        self.assertEqual(expected, d.show())

if __name__ == '__main__':
    unittest.main()