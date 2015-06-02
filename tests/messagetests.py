# -*- coding: utf-8 -*-
""" This script contains tests for the core.message module.
"""

import unittest
from datetime import datetime

import core.message as msg
from core.exceptions import ParametersException

class MessageTest(unittest.TestCase):
    def test_set_default_repeat(self):
        # Bad type raise exception.
        self.assertRaises(ParametersException, msg.set_default_repeat, 'str')
        # Bad values also raise exception.
        self.assertRaises(ParametersException, msg.set_default_repeat, 0)
        self.assertRaises(ParametersException, msg.set_default_repeat, -42)
        # Now test with a good value.
        msg.set_default_repeat(5)
        self.assertEquals(msg.DEFAULT_REPEAT, 5)

    def test_set_default_ttl(self):
        # Bad type raise exception.
        self.assertRaises(ParametersException, msg.set_default_ttl, 'str')
        # Bad values also raise exception.
        self.assertRaises(ParametersException, msg.set_default_ttl, 0)
        self.assertRaises(ParametersException, msg.set_default_ttl, -42)
        # Now test with a good value.
        msg.set_default_ttl(42)
        self.assertEquals(msg.DEFAULT_TTL, 42)

    def test_set_default_duration(self):
        # Bad type raise exception.
        self.assertRaises(ParametersException, msg.set_default_duration, 'str')
        # Bad values also raise exception.
        self.assertRaises(ParametersException, msg.set_default_duration, 0)
        self.assertRaises(ParametersException, msg.set_default_duration, -42)
        # Now test with a good value.
        msg.set_default_duration(10)
        self.assertEquals(msg.DEFAULT_DURATION, 10)

    def test_is_outdated(self):
        message = msg.Message("Some contents", "My app", 5, 1, 5, {})
        message.added_date = datetime(1970,1,1)
        self.assertTrue(message.is_outdated())

        message.added_date = datetime.now()
        self.assertFalse(message.is_outdated())

    def test_create_message_from_dict_no_contents(self):
        # Test with 'contents' that is not present in the dict.
        dico = {'sender': 'My app'}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_contents_not_str(self):
        # Test with 'contents' that is not a string.
        dico = {'contents': 42, 'sender': 'My app'}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_no_sender(self):
        # Test with 'sender' that is not present in the dict.
        dico = {'contents': 'A message.'}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_sender_not_str(self):
        # Test with 'sender' that is not a string.
        dico = {'contents': 'A message.', 'sender': 42}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_no_ttl(self):
        # Set up default ttl.
        msg.set_default_ttl(60)
        # Test with 'ttl' that is not in dict.
        dico = {'contents': 'A message.', 'sender': 'My app'}
        message = msg.create_message_from_dict(dico)
        self.assertEquals(message.ttl, msg.DEFAULT_TTL)

    def test_create_message_from_dict_ttl_not_int(self):
        # Test with 'ttl' that is not a int.
        dico = {'contents': 'A message.', 'sender': 'My app', 'ttl': '5'}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_bad_ttl(self):
        # Test with bad 'ttl' values.
        dico = {'contents': 'A message.', 'sender': 'My app', 'ttl': 0}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

        dico = {'contents': 'A message.', 'sender': 'My app', 'ttl': -42}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_no_repeat(self):
        # Set up default repeat.
        msg.set_default_repeat(1)
        # Test with 'repeat' that is not in dict.
        dico = {'contents': 'A message.', 'sender': 'My app'}
        message = msg.create_message_from_dict(dico)
        self.assertEquals(message.repeat, msg.DEFAULT_REPEAT)

    def test_create_message_from_dict_repeat_not_int(self):
        # Test with 'repeat' that is not a int.
        dico = {'contents': 'A message.', 'sender': 'My app', 'repeat': '5'}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_bad_repeat(self):
        # Test with bad 'repeat' values.
        dico = {'contents': 'A message.', 'sender': 'My app', 'repeat': 0}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

        dico = {'contents': 'A message.', 'sender': 'My app', 'repeat': -42}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_no_duration(self):
        # Set up default duration.
        msg.set_default_duration(10)
        # Test with 'duration' that is not in dict.
        dico = {'contents': 'A message.', 'sender': 'My app'}
        message = msg.create_message_from_dict(dico)
        self.assertEquals(message.duration, msg.DEFAULT_DURATION)

    def test_create_message_from_dict_not_int(self):
        # Test with 'duration' that is not a int.
        dico = {'contents': 'A message.', 'sender': 'My app', 'duration': '10'}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

    def test_create_message_from_dict_bad_duration(self):
        # Test with bad 'duration' values.
        dico = {'contents': 'A message.', 'sender': 'My app', 'duration': 0}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)

        dico = {'contents': 'A message.', 'sender': 'My app', 'duration': -42}
        self.assertRaises(ParametersException, msg.create_message_from_dict, dico)
