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

def check_type(variable, typeExpected, keyName):
    """ Check that the type of the variable match with the expected type.
        If not, raise a ParametersException with BAD_PARAMETER_TYPE code.
        Else, do nothing.

    Keyword Arguments:
        variable     - The variable to check.
        typeExpected - The type expected.
        keyName      - A string used to build the message of the exception.
    """
    if(type(variable) != typeExpected):
        raise ParametersException("'"+keyName+ \
                                  "'' is not a "+str(typeExpected)+".",
                                  exceptions.BAD_PARAMETER_TYPE)

def check_is_positive(variable, keyName):
    """ Check that the variable is > 0.
        If not, raise a ParametersException with BAD_PARAMETER_VALUE code.
        Else, do nothing.

    Keyword Arguments:
        variable - The variable to check.
        keyName  - A string used to build the message of the exception.
    """
    if variable <= 0:
        raise ParametersException("'"+keyName+"' must be > 0.",
                                  exceptions.BAD_PARAMETER_VALUE)

def create_message_from_dict(dictionnary):
    """ Create a Message object from a dictionnary given in parameters.
        Typically, this dictionnary comes from a JSON.

    Keyword Arguments:
        dictionnary - A dictionnary that holds at least 'contents',
                      'sender' and 'ttl' keys.
    """
    copied_dict = copy.copy(dictionnary)
    # Manage contents and sender.
    for key in ('contents', 'sender'):
        if key not in copied_dict:
            raise ParametersException("'"+key+"' is not in the dictionnary.",
                                        exceptions.MISSING_PARAMETER)
        check_type(copied_dict[key], str, key)
    default_values_dict = {'ttl':DEFAULT_TTL,
                           'duration': DEFAULT_DURATION,
                           'repeat': DEFAULT_REPEAT}
    # Managed ttl, duration and repeat.
    for key in ('ttl', 'repeat', 'duration'):
        value = default_values_dict[key]
        if key in copied_dict:
            value = copied_dict[key]
            check_type(value, int, key)
            check_is_positive(value, key)
        copied_dict[key] = value
    m = Message(copied_dict['contents'], copied_dict['sender'],
                copied_dict['ttl'], copied_dict['repeat'],
                copied_dict['duration'], {})
    # Remove managed params from the dict to create other_params.
    other_params = copied_dict
    for key in ('contents', 'sender', 'ttl', 'duration', 'repeat'):
        del(copied_dict[key])
    m.other_params = copied_dict
    return m
