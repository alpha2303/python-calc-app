from .datatype import IDataType

"""
Integer - Class Wrapper for Integer datatypes

Inherits DataType Interface
"""
class Integer(IDataType):
    def __init__(self, a):
        self.value = a
    
    def __add__(self, other):
        return Integer(self.value + other.value)
    
    def __sub__(self, other):
        return Integer(self.value - other.value)
    
    def __mul__(self, other):
        return Integer(self.value * other.value)
    
    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError
        return Integer(self.value / other.value)
    
    def to_string(self) -> str:
        return str.format("{}", self.value)