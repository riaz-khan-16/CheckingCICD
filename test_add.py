from main import add, subtraction

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_sub():
    assert subtraction(2,3)==-1
    