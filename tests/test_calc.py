import pytest
from calcapp.calc import add, subtract, product

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_product():
    assert product(4, 3) == 12

@pytest.mark.parametrize("a,b", [(0,1), (1,0), (-1,2), (2,-1)])
def test_positive_only(a,b):
    with pytest.raises(ValueError):
        add(a,b)

def test_type_check():
    with pytest.raises(ValueError):
        product("2", 3)  # not ints
