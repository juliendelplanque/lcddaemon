#-*- coding: utf-8 -*-
""" This script defines exceptions related to drivers.
"""

class DriverException(Exception):
    pass

class BadNumberOfString(DriverException):
    """ This exception is raised when the number of line to display given to
        the driver does not match the number of line(s) available.
    """
    def __str__(self):
        return 'The number of line to display does not match the number of'+\
               ' line(s) available.'
