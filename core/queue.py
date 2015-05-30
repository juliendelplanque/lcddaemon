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
        message.set_added_date_now()
        print("Message added in the queue - "+str(message.added_date))

    def __str__(self):
        """ Create a string representation of the queue.
        """
        string = "MessageQueue[Head - "
        for message in self.queue.queue:
            string += str(message)+" - "
        return string+"Tail]"
