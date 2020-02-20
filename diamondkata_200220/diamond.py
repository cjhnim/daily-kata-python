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
            bottom = self.buildBottom(c, line, bottom)

        return top + bottom

    def buildTop(self, line, top):
        top += line
        return top

    def buildBottom(self, c, line, bottom):
        return line + bottom if chr(c) != self.upTo else bottom

    def buildLine(self, c):
        line = self.outerSpaces(c) + \
            c + \
            self.innerSpaces(c) + \
            self.secondLetter(c) + \
            '\n'
        return line

    def innerSpaces(self, c):
        count = (ord(c) - ord(self.START_LETTER))*2-1
        return self.makeSpaces(count) if c != self.START_LETTER else ''

    def makeSpaces(self, count):
        spaces = ''
        for n in range(0, count):
            spaces = self.buildTop(' ', spaces)
        return spaces

    def outerSpaces(self, c):
        count = ord(self.upTo) - ord(c)
        return self.makeSpaces(count) if c != self.upTo else ''

    def secondLetter(self, c):
        return c if c != self.START_LETTER else ''
