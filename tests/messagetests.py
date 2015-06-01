# -*- coding: utf-8 -*-
""" This script contains tests for the core.message module.
"""

import unittest

import core.message as msg
from core.exceptions import ParametersException

class MessageTest(unittest.TestCase):
    def test_set_default_repeat(self):
        # Must be None at start.
        self.assertIsNone(msg.DEFAULT_REPEAT)
        # Bad type raise exception.
        self.assertRaises(ParametersException, msg.set_default_repeat, 'str')
        # Bad values also raise exception.
        self.assertRaises(ParametersException, msg.set_default_repeat, 0)
        self.assertRaises(ParametersException, msg.set_default_repeat, -42)
        # Now test with a good value.
        msg.set_default_repeat(5)
        self.assertEquals(msg.DEFAULT_REPEAT, 5)

    def test_set_default_ttl(self):
        # Must be None at start.
        self.assertIsNone(msg.DEFAULT_TTL)
        # Bad type raise exception.
        self.assertRaises(ParametersException, msg.set_default_ttl, 'str')
        # Bad values also raise exception.
        self.assertRaises(ParametersException, msg.set_default_ttl, 0)
        self.assertRaises(ParametersException, msg.set_default_ttl, -42)
        # Now test with a good value.
        msg.set_default_ttl(42)
        self.assertEquals(msg.DEFAULT_TTL, 42)

    def test_set_default_duration(self):
        # Must be None at start.
        self.assertIsNone(msg.DEFAULT_DURATION)
        # Bad type raise exception.
        self.assertRaises(ParametersException, msg.set_default_duration, 'str')
        # Bad values also raise exception.
        self.assertRaises(ParametersException, msg.set_default_duration, 0)
        self.assertRaises(ParametersException, msg.set_default_duration, -42)
        # Now test with a good value.
        msg.set_default_duration(10)
        self.assertEquals(msg.DEFAULT_DURATION, 10)
