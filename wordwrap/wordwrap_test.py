import wordwrap as ww

def test_exception():
    assert ww.Wrapper.wrap("", 0) == ""

def test_one_word():
    assert ww.Wrapper.wrap("word", 4) == "word"

def test_break_line():
    assert ww.Wrapper.wrap("word word", 4) == "word--word"

def test_find_space():
    assert ww.Wrapper.wrap("word word", 5) == "word--word"

def test_wrap_in_word():
    assert ww.Wrapper.wrap("word wordword", 7) == "word wo--rdword"

def test_recursive():
    assert ww.Wrapper.wrap("word word word", 4) == "word--word--word"

def test_word_length():
    assert ww.Wrapper.wrap("word word word", 5) == "word--word--word"
