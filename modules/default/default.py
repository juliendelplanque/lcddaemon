#-*- coding: utf-8 -*-
""" This script contains the module that will be used by default if the user
    doesn't specify anything.
"""

from modules.abstractmodule import AbstractModule

class Default(AbstractModule):
    """ This module does absolutely nothing.
    """
    def apply_actions_to(self, message):
        """ Do nothing.
        """
        pass
