from .entry_handler import IEntryHandler
from common import Complex

"""
ComplexHandler - Class providing input handling for Complex Number datatypes

Inherits IEntryHandler interface
"""
class ComplexEntryHandler(IEntryHandler):
    
    @staticmethod
    def get_input():
        num = float(input("Enter real component: "))
        den = float(input("Enter imaginary component: "))
        return Complex(num, den)