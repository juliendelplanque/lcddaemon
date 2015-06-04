#-*- coding: utf-8 -*-
""" This script contains the definition of an abstract module.
"""

class AbstractModule(object):
    """ This defines the method(s) that all lcddaemon module must implement.
    """
    def apply_actions_with(message):
        """ This method is called by the thread that pop() messages from the
            MessageQueue.

        Keyboard Arguments:
            message - The message pop from the queue.
        """
        raise NotImplementedError()
