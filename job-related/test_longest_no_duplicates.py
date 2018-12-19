import pytest

def test_empty_string():
    from longestSubstringNoDuplicates import lengthOfLongestSubstring
    assert lengthOfLongestSubstring('') == ''

def test_string_of_one_char():
    from longestSubstringNoDuplicates import lengthOfLongestSubstring
    assert lengthOfLongestSubstring('a') == 'a'

def test_one_char_with_duplicate():
    from longestSubstringNoDuplicates import lengthOfLongestSubstring
    assert lengthOfLongestSubstring('aa') == 'a'

def test_two_chars_no_duplicates():
    from longestSubstringNoDuplicates import lengthOfLongestSubstring
    assert lengthOfLongestSubstring('ab') == 'ab'

def test_three_chars_exclude_duplicate():
    from longestSubstringNoDuplicates import lengthOfLongestSubstring
    assert lengthOfLongestSubstring('aba') == 'ab'

'''
def test_multi_substrings_no_duplicates():
    from longestSubstringNoDuplicates import lengthOfLongestSubstring
    assert lengthOfLongestSubstring('abcabqrstuvwxyz') == 'qrstuvwxyz'
    '''