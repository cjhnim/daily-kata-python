import unittest
# import diamond

class Diamond:
    START_LETTER = 'A'
    ENTER = '\n'
    SPACE = ' '
    BLANK = ''

    def __init__(self, upTo):
        self.upTo = upTo
    
    def show(self):
        top = self.BLANK
        bottom = self.BLANK
        
        for c in range(ord(self.START_LETTER), ord(self.upTo)+1):
            line = self.buildLine(chr(c))
            top += line
            if(chr(c) != self.upTo):
                bottom = line + bottom

        return top + bottom

    def buildLine(self, c):
        line = self.indent(c)
        line += c
        if c != self.START_LETTER:
            line += self.innerSpace(c)
            line += c
        line += self.ENTER
        return line

    def indent(self, c):
        count = ord(self.upTo) - ord(c)
        return self.makeSpace(count)

    def innerSpace(self, c):
        index = ord(c) - ord(self.START_LETTER)
        count = index*2-1
        return self.makeSpace(count)

    def makeSpace(self, count):
        space = ''
        for i in range(0, count):
            space += self.SPACE
        return space



            

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

if __name__ == '__main__':
    unittest.main()
