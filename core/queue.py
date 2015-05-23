#-*- coding: utf-8 -*-
""" This script defines the queue object used to hold
    messages to be displayed by a LCD screen.
"""

from queue import Queue

class MessageQueue(object):
    """ This object hold messages that will be displayed
        on a LCD screen.
    """
    def __init__(self):
        self.queue = Queue()

    def pop(self):
        """ Pop the first message from the queue.
            This operation is thread-safe.
        """
        return self.queue.get()

    def put(self, message):
        """ Put a message at the end of the queue.
            This operation is thread-safe.
        """
        self.queue.put(message)
