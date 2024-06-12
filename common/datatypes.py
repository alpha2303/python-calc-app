
"""
DataType - Inteface for creating datatypes for the calculator

Classes inheriting this interface needs to implement the corresponding
magic methods (__methodname__()) to support binary operations, else 
the operations will throw `NotImplementedError` exception.
"""
class DataType:

    # Addition
    def __add__(self, other):
        raise NotImplementedError
    
    # Subtraction
    def __sub__(self, other):
        raise NotImplementedError
    
    # Multiplication
    def __mul__(self, other):
        raise NotImplementedError
    
    # Division
    def __truediv__(self, other):
        raise NotImplementedError

"""
Integer - Class Wrapper for Integer datatypes

Inherits DataType Interface
"""
class Integer(DataType):
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