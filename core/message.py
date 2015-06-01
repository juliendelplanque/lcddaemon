#-*- coding: utf-8 -*-
""" This script defines the message object used to represent
    a message to display on a LCD screen.
"""

import copy
from datetime import datetime
from datetime import timedelta

import core.exceptions as exceptions # for error codes constants
from core.exceptions import ParametersException

DEFAULT_REPEAT   = None
DEFAULT_TTL      = None
DEFAULT_DURATION = None

def verify_new_int_global(varToVerify, name):
    """ Verify that varToVerify is an integer > 0.
        If it is not, raise an ParametersException.

    Keyword Arguments:
        varToVerify - The variable to verify.
        name        - The name to put in the exception message.
    """
    if type(varToVerify) != int:
        raise ParametersException("'"+name+"' is not an integer.",
                                    exceptions.BAD_PARAMETER_TYPE)
    if varToVerify <= 0:
        raise ParametersException("'"+name+"' must be > 0.",
                                    exceptions.BAD_PARAMETER_VALUE)

def set_default_repeat(numberOfRepetition):
    """ Set the default number of repetition of a message.

    Keyword Arguments:
        numberOfRepetition - The default number of repetition of a message.
    """
    global DEFAULT_REPEAT
    verify_new_int_global(numberOfRepetition, 'repeat')
    DEFAULT_REPEAT = numberOfRepetition

def set_default_ttl(newTtl):
    """ Set the default ttl of a message.

    Keyword Arguments:
        newTtl - The default ttl of a message.
    """
    global DEFAULT_TTL
    verify_new_int_global(newTtl, 'ttl')
    DEFAULT_TTL = newTtl

def set_default_duration(newDuration):
    """ Set the default duration of a message.

    Keyword Arguments:
        newDuration - The default duration of a message.
    """
    global DEFAULT_DURATION
    verify_new_int_global(newDuration, 'duration')
    DEFAULT_DURATION = newDuration

class Message(object):
    """ This object is a message to display on a LCD screen.
    """
    def __init__(self, contents, sender, ttl, repeat, duration, other_params):
        """ Constructor for a Message object.

        Keyword Arguments:
            contents     - A string that will be displayed on the LCD screen.
            sender       - The name of the message's sender.
            ttl          - The time to live of the message.
            repeat       - The number of time the message has to be re-put in
                           the queue.
            duration     - The time that the message has to be display on the
                           screen.
            other_params - Misc parameters.
        """
        self.contents = contents
        self.sender = sender
        self.ttl = ttl
        self.repeat = repeat
        self.duration = duration
        self.other_params = other_params

    def __str__(self):
        """ Return a string representation of the message.
        """
        return "("+self.sender+":"+self.contents+"|"+str(self.ttl)+"s)"

    def set_added_date_now(self):
        self.added_date = datetime.now()

    def is_outdated(self):
        return datetime.now() > self.added_date + timedelta(seconds=self.ttl)

def create_message_from_dict(dictionnary):
    """ Create a Message object from a dictionnary given in parameters.
        Typically, this dictionnary comes from a JSON.

    Keyword Arguments:
        dictionnary - A dictionnary that holds at least 'contents',
                      'sender' and 'ttl' keys.
    """
    copied_dict = copy.copy(dictionnary)
    contents = copied_dict['contents']
    if type(contents) != str:
        raise ParametersException("'contents' is not a string.",
                                    exceptions.BAD_PARAMETER_TYPE)
    sender = copied_dict['sender']
    if type(sender) != str:
        raise ParametersException("'sender' is not a string.",
                                    exceptions.BAD_PARAMETER_TYPE)
    ttl = DEFAULT_TTL
    if 'ttl' in copied_dict:
        ttl = copied_dict['ttl']
        if type(ttl) != int:
            raise ParametersException("'ttl' is not an integer.",
                                        exceptions.BAD_PARAMETER_TYPE)
        if ttl <= 0:
            raise ParametersException("'ttl' must be > 0.",
                                        exceptions.BAD_PARAMETER_VALUE)
        del(copied_dict['ttl'])
    repeat = DEFAULT_REPEAT
    if 'repeat' in copied_dict:
        repeat = copied_dict['repeat']
        if type(repeat) != int:
            raise ParametersException("'repeat' is not an integer.",
                                    exceptions.BAD_PARAMETER_TYPE)
        if repeat <= 0:
            raise ParametersException("'repeat' must be > 0.",
                                    exceptions.BAD_PARAMETER_VALUE)
        del(copied_dict['repeat'])
    duration = DEFAULT_DURATION
    if 'duration' in copied_dict:
        duration = copied_dict['duration']
        if type(duration) != int:
            raise ParametersException("'duration' is not an integer.",
                                    exceptions.BAD_PARAMETER_TYPE)
        if duration <= 0:
            raise ParametersException("'duration' must be > 0.",
                                    exceptions.BAD_PARAMETER_VALUE)
        del(copied_dict['duration'])
    del(copied_dict['contents'])
    del(copied_dict['sender'])
    return Message(contents=contents, sender=sender, ttl=ttl,
                    repeat=repeat, duration=duration, other_params=copied_dict)
