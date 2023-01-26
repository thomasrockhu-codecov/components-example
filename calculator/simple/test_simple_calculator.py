from .simple_calculator import Calculator

def test_add():
    assert Calculator.add(1, 2) == 3.0
