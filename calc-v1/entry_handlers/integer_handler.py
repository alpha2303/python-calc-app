from .entry_handler import IEntryHandler
from common import Integer

"""
IntegerHandler - Class providing input handling for Integer datatypes

Inherits IEntryHandler interface
"""
class IntegerEntryHandler(IEntryHandler):
    
    @staticmethod
    def get_input():
        return Integer(int(input("Enter integer: ")))