from src.maths_operations import add, sub

def test_add():
    assert add(1,3)==4
    assert add(3,4)==7
    assert add(2,6)==8

def sub_add():
    assert sub(5,4)==1
    assert sub(6,4)==2
    assert sub(8,3)==5

    