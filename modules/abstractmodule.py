#-*- coding: utf-8 -*-
""" This script contains the definition of an abstract module.
"""

class AbstractModule(object):
    """ This defines the method(s) that all lcddaemon module must implement.
    """
    def apply_actions_to(self, message):
        """ This method is called by the thread that pop() messages from the
            MessageQueue BEFORE the message is displayed.

        Keyboard Arguments:
            message - The message pop from the queue.
        """
        raise NotImplementedError()

    def apply_post_actions_to(self, message):
        """ This method is called by the thread that pop() messages from the
            MessageQueue AFTER the message has been displayed.

        Keyboard Arguments:
            message - The message that has been displayed.
        """
        raise NotImplementedError()
