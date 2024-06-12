"""
IEntryHandler - Interface for handler classes that provide input interface for various datatypes
"""
class IEntryHandler:
    @staticmethod
    def get_input():
        raise NotImplementedError