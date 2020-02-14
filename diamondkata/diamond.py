
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
            bottom = self.bottomLine(chr(c), line, bottom)

        return top + bottom

    def bottomLine(self, c, line, bottom):
        return line + bottom if(c != self.upTo) else bottom

    def buildLine(self, c):
        return self.indent(c) + \
                self.letter(c) + \
                self.innerSpace(c) + \
                self.secondLetter(c) + \
                self.ENTER
    
    def letter(self, c):
        return c

    def secondLetter(self, c):
        return c if c != self.START_LETTER else ''

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

        