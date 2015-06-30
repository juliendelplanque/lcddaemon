#-*- coding: utf-8 -*-
""" This script contains the abstract animation object that must be implemented
    by all animation extension.
"""

class AbstractAnimation(object):
    """ An abstract animation that defines method(s) that must be implemented
        by animation extensions.
    """
    def __init__(self, driver):
        self.driver = driver

    def animate(self, message):
        """ This method is called by the thread that pop() messages from the
            MessageQueue.

            It's in this method that there is a "discution" with the driver to
            tell it how to display the message in a beautiful way (or not, you
            decide it after all!).

        Keyboard Arguments:
            message - The message pop from the queue.
        """
        raise NotImplementedError()
