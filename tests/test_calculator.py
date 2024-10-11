import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_perform_operation_add(calc):
    assert calc.perform_operation("add", 5, 3) == 8

def test_perform_operation_subtract(calc):
    assert calc.perform_operation("subtract", 5, 3) == 2

def test_perform_operation_multiply(calc):
    assert calc.perform_operation("multiply", 5, 3) == 15

def test_perform_operation_divide(calc):
    assert calc.perform_operation("divide", 6, 3) == 2
    with pytest.raises(ValueError):
        calc.perform_operation("divide", 5, 0)

def test_perform_operation_modulus(calc):
    assert calc.perform_operation("modulus", 5, 3) == 2

def test_perform_operation_power(calc):
    assert calc.perform_operation("power", 2, 3) == 8

def test_history_full(calc):
    calc.perform_operation("add", 2, 3)
    calc.perform_operation("subtract", 5, 2)
    assert len(calc.get_history()) == 2

def test_history_last(calc):
    calc.perform_operation("add", 2, 3)
    assert calc.get_history(last_only=True) == ["Add: 2 and 3 = 5"]
