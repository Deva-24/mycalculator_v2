from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddOperation(Operation):
    def execute(self, a, b):
        return a + b

class SubtractOperation(Operation):
    def execute(self, a, b):
        return a - b

class MultiplyOperation(Operation):
    def execute(self, a, b):
        return a * b

class DivideOperation(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class ModulusOperation(Operation):
    def execute(self, a, b):
        return a % b

class PowerOperation(Operation):
    def execute(self, a, b):
        return a ** b
