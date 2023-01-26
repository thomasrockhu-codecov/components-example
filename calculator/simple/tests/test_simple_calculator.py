from ..controllers.simple_calculator import Calculator

def test_add():
    assert Calculator.add(1, 2) == 3.0

def test_subtract():
    assert Calculator.subtract(5, 17) == -12.0
