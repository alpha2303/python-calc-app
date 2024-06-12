from .input_handler import IInputHandler
from common import Complex

"""
ComplexHandler - Class to provide input interface for Complex Number datatypes

Inherits IInputHandler interface
"""
class ComplexHandler(IInputHandler):
    
    @staticmethod
    def get_input():
        num = float(input("Enter real component: "))
        den = float(input("Enter imaginary component: "))
        return Complex(num, den)