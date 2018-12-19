import pytest

def test_empty_array():
    from subsets import getSubsets
    assert getSubsets([]) == []

def test_array_len_one():
    from subsets import getSubsets
    assert getSubsets([1]) == [1]

def test_simple_array():
    from subsets import getSubsets
    assert getSubsets([1,2]) == [[1,2], [1], [2]]