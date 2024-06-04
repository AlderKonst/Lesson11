import math

lst = [1, 45, 75, 8, 4, 2, 24, 7]

def test_sorted():
    assert sorted(lst) == [1, 2, 4, 7, 8, 24, 45, 75]

def test_map():
    assert list(map(lambda x: x**2, lst)) == [1, 2025, 5625, 64, 16, 4, 576, 49]

def test_filter():
    assert list(filter(lambda x: x > 10, lst)) == [45, 75, 24]

def test_pi():
    assert round(math.pi, 5)  == 3.14159

def test_sqrt():
    assert math.sqrt(64) == 8

def test_pow():
    assert math.pow(3, 3) == 27

def test_hypot():
    assert round(math.hypot(3, 2), 5) == 3.60555