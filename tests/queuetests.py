# -*- coding: utf-8 -*-
""" This script contains tests for the core.queue module.
"""

import unittest
from datetime import datetime

from core.message import Message
from core.queue import MessageQueue

class MessageQueueTest(unittest.TestCase):
    def test_put_pop_users(self):
        q = MessageQueue(2)
        self.assertEquals(len(q.users.keys()), 0)
        q.put(Message('contents', 'sender', 5, 1, 10, {}))
        self.assertTrue('sender' in q.users)
        self.assertEquals(q.users['sender'].message_count, 1)
        q.put(Message('contents', 'sender2', 5, 1, 10, {}))
        self.assertTrue('sender2' in q.users)
        self.assertEquals(q.users['sender2'].message_count, 1)
        q.pop()
        self.assertEquals(q.users['sender'].message_count, 0)
        q.pop()
        self.assertEquals(q.users['sender2'].message_count, 0)

    def test_pop_outdated(self):
        q = MessageQueue(2)
        m = Message('this message will be ignored', 'sender', 5, 1, 10, {})
        q.put(m)
        m.added_date = datetime(1970, 1, 1)
        q.put(Message('this message will be poped!', 'sender', 5, 1, 10, {}))
        self.assertEquals(q.pop().contents, 'this message will be poped!')

    def test_user_reached_limit(self):
        q = MessageQueue(2)
        q.put(Message('contents', 'sender', 5, 1, 10, {}))
        self.assertFalse(q.user_reached_limit('sender'))
        q.put(Message('contents', 'sender', 5, 1, 10, {}))
        self.assertTrue(q.user_reached_limit('sender'))
