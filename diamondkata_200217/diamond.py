class Diamond:
    START_LETTER = 'A'

    def __init__(self, upTo):
        self.upTo = upTo

    def show(self):
        top = ''
        bottom = ''
        
        for c in range(ord(self.START_LETTER), ord(self.upTo)+1):
            line = self.buildLine(chr(c))
            top = self.buildTop(line, top)
            bottom = self.buildBottom(chr(c), line, bottom)
        return top + bottom

    def buildLine(self, c):
        return self.indent(c) + \
                self.firstLetter(c) + \
                self.secondIndent(c) + \
                self.secondLetter(c) + \
                '\n'

    def firstLetter(self, c):
        return c
    def secondLetter(self, c):
        return c if c != self.START_LETTER else ''

    def indent(self, c):
        count = ord(self.upTo)-ord(c)
        return self.buildSpace(count)

    def buildSpace(self, count):
        space = ''
        for n in range(0, count):
            space += ' '
        return space

    def secondIndent(self, c):
        return ' ' if c != self.START_LETTER else ''
        
    def buildTop(self, line, top):
        return top + line

    def buildBottom(self, c, line, bottom):
        return line + bottom if self.upTo != c else bottom