#-*- coding: utf-8 -*-
""" This script defines exceptions that can be raised by the applications.
"""

# Parameters errors
BAD_PARAMETER_TYPE  = 101
BAD_PARAMETER_VALUE = 102

# Spamming error
TOO_MUCH_MESSAGES   = 201

# Missing parameter error
MISSING_PARAMETER   = 301

class LCDException(Exception):
    """ This is the abstract exception from which all exceptions created for
        this app should inherit.
    """
    def __init__(self, cause, code):
        """ Constructor for the LCDException object.

        Keyword Arguments:
            cause - A string that explains the cause of the exception.
            code  - An integer that is one of the constants defined in this
                    module.
        """
        self.cause = cause
        self.code = code

    def __str__(self):
        return str(self.cause)

class ParametersException(LCDException):
    """ This exception is raised when a parameter has a bade type or a bad
        value.
    """
    pass

class UserException(LCDException):
    """ This exception is raised when the user is doing something wrond
        with his requests.
    """
    pass
