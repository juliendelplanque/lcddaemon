#-*- coding: utf-8 -*-
""" This script contains an example of module that simply print the message pop
    from the queue.
"""

from modules.abstractmodule import AbstractModule

class Printer(AbstractModule):
    """ A module that print the contents of a message when apply_actions_with
        method is called.
    """
    def apply_actions_with(self, message):
        """ Simply print the message's contents with my name before.
        """
        print("Printer: "+message.contents)
