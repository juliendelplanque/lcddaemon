#-*- coding: utf-8 -*-
""" This script defines the message object used to represent
    a message to display on a LCD screen.
"""

import copy

class Message(object):
    """ This object is a message to display on a LCD screen.
    """
    def __init__(self, content, sender, **kwargs):
        self.content = content
        self.sender = sender
        self.other_params = kwargs

    def __str__(self):
        """ Return a string representation of the message.
        """
        return "("+self.sender+":"+self.content+")"

def create_message_from_dict(dictionnary):
    copied_dict = copy.copy(dictionnary)
    content = copied_dict['content']
    sender = copied_dict['sender']
    del(copied_dict['content'])
    del(copied_dict['sender'])
    return Message(content=content, sender=sender, kwargs=copied_dict)
