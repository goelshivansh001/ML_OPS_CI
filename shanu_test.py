import pytest

def square(n):
    return n**2
def cube(n):
    return n**3
def fifth(n):
    return n**5


def test_square():
    assert square(2)==4, "Test Failed Square of the 2 musr be 4"
    assert square(3)==9, "Test Failed Square of the 3 must be 9"


def test_cube():
    assert cube(2)==8, "Test Failed Cube of the 2 must be 8"
    assert cube(3)==27, "Test Failed Cube of the 3 must be 27"

def test_fifth():
    assert fifth(2)==32, "Test Failed Cube of the 2 must be 32"
    assert fifth(3)==243, "Test Failed Cube of the 3 must be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("String")