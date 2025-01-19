import pytest

from calculaater import square

def main():
    test_postive()


#def test_square():
#   if square(2)!=4:
#        print("2 squared was not 4")
#    if square(3)!=9:
#        print("3 squared was not 9")
#    if square(0)!=0:
#        print("0 squared was not 0")

#def test_square():
#    assert square(2)==4
#    assert square(3)==9
#    assert square(0)==0
#    assert square(-2)==4

def test_postive():
    assert square(2)==4
    assert square(3)==9

def test_negative():
    assert square(-2)==4
    assert square(-3)==9

def test_zero():
    assert square(0)==0

def test_str():
     with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()    