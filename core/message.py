#-*- coding: utf-8 -*-
""" This script defines the message object used to represent
    a message to display on a LCD screen.
"""
class Message(object):
    """ This object is a message to display on a LCD screen.
    """
    def __init__(self, content, sender, **kwargs):
        self.content = content
        self.sender = sender
        self.other_params = kwargs
