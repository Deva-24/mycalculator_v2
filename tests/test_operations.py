import pytest
from app.operations import (
    AddOperation, SubtractOperation, MultiplyOperation,
    DivideOperation, ModulusOperation, PowerOperation
)

@pytest.fixture
def operations():
    return {
        "add": AddOperation(),
        "subtract": SubtractOperation(),
        "multiply": MultiplyOperation(),
        "divide": DivideOperation(),
        "modulus": ModulusOperation(),
        "power": PowerOperation(),
    }

def test_add(operations):
    assert operations["add"].execute(5, 3) == 8

def test_subtract(operations):
    assert operations["subtract"].execute(5, 3) == 2

def test_multiply(operations):
    assert operations["multiply"].execute(5, 3) == 15

def test_divide(operations):
    assert operations["divide"].execute(6, 3) == 2
    with pytest.raises(ValueError):
        operations["divide"].execute(5, 0)

def test_modulus(operations):
    assert operations["modulus"].execute(5, 3) == 2

def test_power(operations):
    assert operations["power"].execute(2, 3) == 8
