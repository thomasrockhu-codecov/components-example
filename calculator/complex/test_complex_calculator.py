from .complex_calculator import ComplexCalculator

def test_multiply():
    assert ComplexCalculator.multiply(1, 2) == 2

def test_divide():
    assert ComplexCalculator.divide(1, 2) == 0.5
