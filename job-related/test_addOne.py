import pytest

def test_empty_array():
    from addOne import addOneToArray
    assert addOneToArray([]) == [1]

def test_add_no_carry():
    from addOne import addOneToArray
    assert addOneToArray([4]) == [5]

def test_add_with_carry():
    from addOne import addOneToArray
    assert addOneToArray([9]) == [1,0]

def test_add_one_to_larger_array():
    from addOne import addOneToArray
    assert addOneToArray([1,2,3,4,5,6,7,8]) == [1,2,3,4,5,6,7,9]

def test_add_larger_array_with_carry():
    from addOne import addOneToArray
    assert addOneToArray([1,2,3,4,5,6,7,8,9]) == [1,2,3,4,5,6,7,9,0]

def test_multi_carry():
    from addOne import addOneToArray
    assert addOneToArray([9,9,9]) == [1,0,0,0]

