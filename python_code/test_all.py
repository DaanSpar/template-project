import pytest

from main import *

def test_example():
    assert example_fcn_2(3) == 5
    assert example_fcn_2(0) == 1
    assert example_fcn_2(10) == 11
