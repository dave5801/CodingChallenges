import pytest
#Yes, I'm writing test cases, like a good engineer.
def test_empty_string():
    from firstrecur import findFirstRecur
    assert findFirstRecur('') == 'Empty'

def test_no_recurring_chars():
    from firstrecur import findFirstRecur
    assert findFirstRecur('abc') == 'No recurring characters'

def test_first_char_a_recuring_character():
    from firstrecur import findFirstRecur
    assert findFirstRecur('aba') == 'a'

def test_non_first_char_is_recurring():
    from firstrecur import findFirstRecur
    assert findFirstRecur('xaba') == 'a'

def test_multi_recurring_chars_returns_first():
    from firstrecur import findFirstRecur
    assert findFirstRecur("dbcabad") == 'b'