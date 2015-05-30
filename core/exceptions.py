#-*- coding: utf-8 -*-
""" This script defines exceptions that can be raised by the applications.
"""

class ParametersException(Exception):
    """ This exception is raised when a parameter has a bade type or a bad
        value.
    """
    def __init__(self, cause):
        """ Constructor fot he ParametersException object.

        Keyword Arguments:
            cause - A string that explains the cause of the exception.
        """
        self.cause = cause

    def __str__(self):
        return str(self.cause)
