import sys
# sys.path.append('G:/Calculator')
from Calculator.calculator import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0
    assert add(1, -1) == 0
def test_sub():
    assert sub(1, 2) == -1
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0
    assert sub(-1, 1) == -2
    assert sub(1, -1) == 2
def test_mul():
    assert mul(1, 2) == 2
    assert mul(0, 0) == 0
    assert mul(-1, -1) == 1
    assert mul(-1, 1) == -1
    assert mul(1, -1) == -1
def test_div():
    assert div(1, 2) == 0.5
    assert div(0, 0) == "Error! Division by zero."
    assert div(-1, -1) == 1
    assert div(-1, 1) == -1
    assert div(1, -1) == -1
