from .input_handler import IInputHandler
from common import Integer

"""
IntegerHandler - Class to provide input interface for Integer datatypes

Inherits IInputHandler interface
"""
class IntegerHandler(IInputHandler):
    
    @staticmethod
    def get_input():
        return Integer(int(input("Enter integer: ")))