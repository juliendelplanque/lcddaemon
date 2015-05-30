#-*- coding: utf-8 -*-
""" This script defines the message object used to represent
    a message to display on a LCD screen.
"""

import copy
from datetime import datetime

class Message(object):
    """ This object is a message to display on a LCD screen.
    """
    def __init__(self, contents, sender, ttl, repeat, other_params):
        """ Constructor for a Message object.

        Keyword Arguments:
            contents     - A string that will be displayed on the LCD screen.
            sender       - The name of the message's sender.
            ttl          - The time to live of the message.
            repeat       - The number of time the message has to be re-put in
                           the queue.
            other_params - Misc parameters.
        """
        self.contents = contents
        self.sender = sender
        self.ttl = ttl
        self.repeat = repeat
        self.other_params = other_params

    def __str__(self):
        """ Return a string representation of the message.
        """
        return "("+self.sender+":"+self.contents+"|"+str(self.ttl)+"s)"

    def set_added_date_now(self):
        self.added_date = datetime.now()

def create_message_from_dict(dictionnary):
    """ Create a Message object from a dictionnary given in parameters.
        Typically, this dictionnary comes from a JSON.

    Keyword Arguments:
        dictionnary - A dictionnary that holds at least 'contents',
                      'sender' and 'ttl' keys.
    """
    copied_dict = copy.copy(dictionnary)
    contents = copied_dict['contents']
    sender = copied_dict['sender']
    ttl = copied_dict['ttl']
    repeat = 1
    if 'repeat' in copied_dict:
        repeat = copied_dict['repeat']
        del(copied_dict['repeat'])
    del(copied_dict['contents'])
    del(copied_dict['sender'])
    del(copied_dict['ttl'])
    return Message(contents=contents, sender=sender, ttl=ttl,
                    repeat=repeat, other_params=copied_dict)
