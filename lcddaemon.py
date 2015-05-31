#!/usr/bin/env python3
#-*- coding: utf-8 -*-
""" This script is the launcher of the daemon.
"""

from core.daemonargs import parse_arguments
from core.message import set_default_repeat
from core.message import set_default_ttl
from core.message import set_default_duration
from core.queue import MessageQueue
from server.server import run

if __name__ == '__main__':
    config = parse_arguments()
    set_default_repeat(config["ttr"])
    set_default_ttl(config["ttl"])
    set_default_duration(config["ttd"])
    run(MessageQueue(config["limit"]), config["ptl"])
