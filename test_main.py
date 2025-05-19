import pytest
from main import divide

def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, 2) == -5

def test_divide_zero_divisor():
    with pytest.raises(ValueError):
        divide(10, 0)
