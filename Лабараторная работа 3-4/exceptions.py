# exceptions.py

class TreeError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidHeightError(TreeError):
    """Exception raised for errors in the input height."""
    def __init__(self, height, message="Height must be a non-negative integer"):
        self.height = height
        self.message = message
        super().__init__(self.message)

class InvalidRootError(TreeError):
    """Exception raised for errors in the input root."""
    def __init__(self, root, message="Root must be a positive integer"):
        self.root = root
        self.message = message
        super().__init__(self.message)
