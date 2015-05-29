#-*- coding: utf-8 -*-

from core.queue import MessageQueue
from server.server import run

if __name__ == '__main__':
    run(MessageQueue())
