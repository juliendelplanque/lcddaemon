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
from core.loader import load_module_from_conf
from core.loader import load_driver_from_conf
from core.loader import load_animation_from_conf
from server.server import run

def main():
    # Parse args from cmd.
    config = parse_arguments()
    # Set default values.
    set_default_repeat(config["ttr"])
    set_default_ttl(config["ttl"])
    set_default_duration(config["ttd"])
    # Create the message queue.
    message_queue = MessageQueue(config["limit"])
    # Load module, driver and animation according to args.
    module_class = load_module_from_conf(config)
    driver_class = load_driver_from_conf(config)
    driver = driver_class()
    animation_class = load_animation_from_conf(config)
    animation = animation_class(driver)
    # Create the message manager and start the thread.
    message_manager = QueueManager(message_queue, module_class, animation)
    message_manager_thread = threading.Thread(target=message_manager.manage)
    message_manager_thread.daemon = True
    message_manager_thread.start()
    # Start the web server.
    run(message_queue, config["ptl"])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("You killed me.")
        sys.exit(0)
