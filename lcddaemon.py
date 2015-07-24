#!/usr/bin/env python3
#-*- coding: utf-8 -*-
""" This script is the launcher of the daemon.
"""

import sys
import threading

from core.daemonargs import parse_arguments
from core.message import Message
from core.message import set_default_repeat
from core.message import set_default_ttl
from core.message import set_default_duration
from core.queue import MessageQueue
from core.queuemanager import QueueManager
from core.loader import load_module_from_conf
from core.loader import load_driver_from_conf
from core.loader import load_animation_from_conf
from server.server import run
from server.server import shutdown

driver = None

def main():
    global driver
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
    webserver_thread = threading.Thread(target=run, args=(message_queue, config["ptl"]))
    webserver_thread.daemon = True
    webserver_thread.start()
    # Advertise user that everything is working:
    # In cmd.
    print("Daemon ready!")
    # On the screen.
    started_message = Message("Daemon ready!", "lcd_daemon", 1, 1, 5, {})
    message_queue.put(started_message, verbose=False)
    webserver_thread.join()

if __name__ == '__main__':
    try:
        main()
    except:
        # Shutdown the server and advertise the user.
        # In cmd.
        print("Shutting down...")
        # On the screen.
        driver.clear()
        driver.write_lines(("Shutting down...",))
        shutdown()
        # Advertise user that the daemon is stopped:
        # In cmd.
        print("Daemon stopped!")
        # On the screen.
        driver.clear()
        driver.write_lines(("Daemon stopped!",))
        sys.exit(0)
