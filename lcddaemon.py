#!/usr/bin/env python3
#-*- coding: utf-8 -*-
""" This script is the launcher of the daemon.
"""

from core.queue import MessageQueue
from server.server import run

if __name__ == '__main__':
    run(MessageQueue())
