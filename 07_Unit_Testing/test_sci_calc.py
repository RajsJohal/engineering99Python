from sci_calc import *
import pytest

def test_find_sqrt():
    assert find_sqrt(100) == 10.0

def test_find_ceil():
    assert find_ceil(3.14) == 4

def test_divisors():
    assert divisors(6) == [1, 2, 3, 6]

def test_1_in_divisors():
    assert 1 in divisors(13)
    assert 1 in divisors(6)
    assert 1 in divisors(1)

@pytest.mark.skip("Work in Progress") #Decorator
def test_divisors_returns_list():
    assert type(divisors(5)) is list