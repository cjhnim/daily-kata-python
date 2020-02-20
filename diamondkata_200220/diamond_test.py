import unittest
from diamond import Diamond


class DiamondTest(unittest.TestCase):
    def test_can_make_instance(self):
        d = Diamond('A')

    def test_A_has_just_A(self):
        d = Diamond('A')
        expected = "A\n"
        self.assertEqual(expected, d.show())

    def test_B_has_ABBA(self):
        d = Diamond('B')
        expected = \
            " A\n" + \
            "B B\n" + \
            " A\n" 
        self.assertEqual(expected, d.show() )

    def test_C_has_ABBCCBBA(self) :
        d = Diamond('C')
        expected = \
            "  A\n" + \
            " B B\n" + \
            "C   C\n" + \
            " B B\n" + \
            "  A\n"
        self.assertEqual(expected, d.show())

    def test_D_has_ABBCCDDCCBBA(self) :
        d = Diamond('D')
        expected = \
            "   A\n" + \
            "  B B\n" + \
            " C   C\n" + \
            "D     D\n" + \
            " C   C\n" + \
            "  B B\n" + \
            "   A\n"
        self.assertEqual(expected, d.show())        


if __name__ == '__main__':
    unittest.main()
