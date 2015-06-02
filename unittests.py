#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This script is the launcher of the unit tests.
"""

import unittest

from tests.messagetests import MessageTest
from tests.queuetests import MessageQueueTest

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MessageTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(MessageQueueTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
