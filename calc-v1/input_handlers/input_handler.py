"""
IInputHandler - Interface for handler classes that provide input interface for various datatypes
"""
class IInputHandler:
    @staticmethod
    def get_input():
        raise NotImplementedError