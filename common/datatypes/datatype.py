"""
IDataType - Interface for creating datatypes for the calculator

Classes inheriting this interface needs to implement the corresponding
magic methods (__methodname__()) to support binary operations, else 
the operations will throw `NotImplementedError` exception.
"""
class IDataType:

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
    
    def to_string(self) -> str:
        raise NotImplementedError