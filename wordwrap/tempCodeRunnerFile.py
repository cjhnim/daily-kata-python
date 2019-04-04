class Wrapper():
    def __init__(self):
        pass

    @staticmethod
    def wrap(text, limit):
        if len(text) <= limit:
            return text

        space = text.rfind(' ', 0, limit)
        length = Wrapper.word_length(text[space+1:])
        wrap_index = space
        if(length > limit):
            wrap_index = limit
        
        return text[:wrap_index] + "--" + Wrapper.wrap(text[wrap_index:].strip(), limit)
    @staticmethod
    def word_length(text):
        if " " in text:
            return text.find(' ') + 1
        return len(text)
