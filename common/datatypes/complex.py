from .datatype import IDataType

"""
Complex - Class Wrapper for Complex Number datatypes

Inherits DataType Interface
"""
class Complex(IDataType):
    def __init__(self, a: float, b: float):
        self.real: float = a
        self.imag: float = b
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        num = (self.real * other.real) - (self.imag * other.imag)
        den = (self.real * other.imag) + (self.imag * other.real)
        return Complex(num, den)
    
    def __truediv__(self, other):
        conj_other = Complex(other.real, (-1) * other.imag)
        num = self * conj_other
        den = other * conj_other
        return Complex(num.real / den.real, num.imag / den.real)
    
    def to_string(self) -> str:
        return str.format("{:.4f} + {:.4f}i", self.real, self.imag)