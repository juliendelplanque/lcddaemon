#!/usr/bin/env python3
#-*- coding: utf-8 -*-
""" This script is the launcher of the daemon.
"""

import sys
import threading

from core.daemonargs import parse_arguments
from core.message import set_default_repeat
from core.message import set_default_ttl
from core.message import set_default_duration
from core.queue import MessageQueue
from core.queuemanager import QueueManager
from server.server import run

from modules.printer.printer import Printer # To remove, has to be done dynamically

def main():
    config = parse_arguments()
    set_default_repeat(config["ttr"])
    set_default_ttl(config["ttl"])
    set_default_duration(config["ttd"])
    message_queue = MessageQueue(config["limit"])
    message_manager = QueueManager(message_queue, Printer, None) # TODO (None)
    message_manager_thread = threading.Thread(target=message_manager.manage)
    message_manager_thread.daemon = True
    message_manager_thread.start()
    run(message_queue, config["ptl"])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("You killed me.")
        sys.exit(0)
