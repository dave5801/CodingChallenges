import pytest

def test_pass_empty_array():
    from sumPairs import sumPairs
    assert sumPairs([],n=0) == False

def test_pass_array_length_one_returns_false():
    from sumPairs import sumPairs
    assert sumPairs([1],n=1) == False

def test_pass_simple_array_returns_true():
    from sumPairs import sumPairs
    assert sumPairs([1,2,3],n=3) == True

def test_pass_larger_array():
    from sumPairs import sumPairs
    assert sumPairs([3,7,5,11,12],n=8) == True