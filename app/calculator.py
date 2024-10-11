from .operations import (
    AddOperation, SubtractOperation, MultiplyOperation,
    DivideOperation, ModulusOperation, PowerOperation
)

class Calculator:
    def __init__(self):
        self.history = []
        self.operations = {
            "add": AddOperation(),
            "subtract": SubtractOperation(),
            "multiply": MultiplyOperation(),
            "divide": DivideOperation(),
            "modulus": ModulusOperation(),
            "power": PowerOperation()
        }

    def perform_operation(self, operation_name, a, b):
        if operation_name in self.operations:
            operation = self.operations[operation_name]
            result = operation.execute(a, b)
            self.history.append(f"{operation_name.capitalize()}: {a} and {b} = {result}")
            return result
        else:
            raise ValueError(f"Unknown operation '{operation_name}'")

    def get_history(self, last_only=False):
        if last_only:
            return [self.history[-1]] if self.history else []
        return self.history
