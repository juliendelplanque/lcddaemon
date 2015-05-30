#-*- coding: utf-8 -*-
""" This script defines exceptions that can be raised by the applications.
"""

BAD_PARAMETER_TYPE  = 1
BAD_PARAMETER_VALUE = 2

class ParametersException(Exception):
    """ This exception is raised when a parameter has a bade type or a bad
        value.
    """
    def __init__(self, cause, code):
        """ Constructor fot he ParametersException object.

        Keyword Arguments:
            cause - A string that explains the cause of the exception.
        """
        self.cause = cause
        self.code = code

    def __str__(self):
        return str(self.cause)
