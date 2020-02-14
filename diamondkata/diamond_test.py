import unittest
from diamond import Diamond

class DiamondTests(unittest.TestCase):

    def test_new_instance(self):
        d = Diamond('A')

    def test_AisA(self):
        d = Diamond('A')
        self.assertEqual("A\n", d.show())

    def test_BisABBA(self):
        d = Diamond('B')
        expected = " A\n" +\
                   "B B\n" + \
                   " A\n"
             
        self.assertEqual(expected, d.show())
    
    def test_CisABBCCBBA(self):
        d = Diamond('C')
        expected = "  A\n" +\
                   " B B\n" + \
                   "C   C\n" + \
                   " B B\n" + \
                   "  A\n"
             
        self.assertEqual(expected, d.show())
    
    def test_DisABBCCDDBBA(self):
        d = Diamond('D')
        expected = "   A\n" + \
                   "  B B\n" + \
                   " C   C\n" + \
                   "D     D\n" + \
                   " C   C\n" + \
                   "  B B\n" + \
                   "   A\n"
             
        self.assertEqual(expected, d.show())
        

if __name__ == '__main__':
    unittest.main()
