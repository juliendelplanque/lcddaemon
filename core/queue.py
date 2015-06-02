# -*- coding: utf-8 -*-
""" This script defines the queue object used to hold
    messages to be displayed by a LCD screen.
"""

from threading import Lock
from queue import Queue

import core.exceptions as exceptions  # for error codes constants
from core.exceptions import UserException

class User(object):
    """ This object old the number of messages a user has in the queue
        and a semaphore to assure atomicity when decrementing the number
        of messages.
    """
    def __init__(self):
        self.message_count = 0
        self.lock = Lock()

    def decrement(self):
        self.lock.acquire()
        self.message_count -= 1
        self.lock.release()

    def increment(self):
        self.lock.acquire()
        self.message_count += 1
        self.lock.release()

class MessageQueue(object):
    """ This object hold messages that will be displayed
        on a LCD screen.
    """
    def __init__(self, limit_per_user):
        self.limit_per_user = limit_per_user
        self.queue = Queue()
        # This dictionnary's keys will be usernames and its values will be the
        # number of messages in the queue for the user.
        self.users = {}

    def pop(self):
        """ Pop the first message from the queue.
            This operation is thread-safe.
        """
        m = self.queue.get()
        while m.is_outdated():
            self.users[m.sender].decrement()
            m = self.queue.get()
        self.users[m.sender].decrement()
        if m.repeat > 1:
            m.repeat -= 1
            self.put(m)
        return m

    def put(self, message):
        """ Put a message at the end of the queue.
            This operation is thread-safe.
        """
        if self.user_reached_limit(message.sender):
            raise UserException("You have too much messages waiting in the queue.",
                                exceptions.TOO_MUCH_MESSAGES)
        self.queue.put(message)
        message.set_added_date_now()
        if message.sender not in self.users:
            self.users[message.sender] = User()

        self.users[message.sender].increment()
        print("Message added in the queue - "+str(message.added_date))

    def user_reached_limit(self, username):
        """ Check if the user that the name is given in parameter reached its
            messages limit or not.
        """
        if username in self.users:
            return self.users[username].message_count >= self.limit_per_user
        else:
            return False

    def __str__(self):
        """ Create a string representation of the queue.
        """
        string = "MessageQueue[Head - "
        for message in self.queue.queue:
            string += str(message)+" - "
        return string+"Tail]"
