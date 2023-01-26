from ..controllers.complex_calculator import ComplexCalculator

def test_multiply():
    assert ComplexCalculator.multiply(1, 2) == 2

def test_divide():
    assert ComplexCalculator.divide(1, 2) == 0.5
    assert ComplexCalculator.divide(1, 4) == 0.25
    assert ComplexCalculator.divide(3, 4) == 0.75
    assert ComplexCalculator.divide(1, 0) == 'Cannot divide by 0'
    assert ComplexCalculator.divide(3, 0) == 'Cannot divide by 0'
