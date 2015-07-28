# -*- coding: utf-8 -*-
""" This script defines the server object that is used to
    handle clients' messages.
"""

import json
import socketserver

from core.message import *
from core.exceptions import LCDException

message_queue = None
instance = None

class MessageHandler(socketserver.StreamRequestHandler):
    """ This object is the handler for messages.
        Messages are encoded as json.
    """
    def handle(self):
        json_str = str(self.rfile.readline(), 'UTF-8')
        message_dict = json.loads(json_str)
        print("JSON received: "+str(message_dict))
        try:
            m = create_message_from_dict(message_dict)
            print("Message created: "+str(m))
            message_queue.put(m)
            print(str(message_queue))
            self.wfile.write(bytes(self.ok_response(), 'UTF-8'))
        except LCDException as paramsException:
            self.wfile.write(bytes(self.response(paramsException.code, paramsException.cause), 'UTF-8'))

    def response(self, code, message):
        return json.dumps({'code': code, 'message': message})

    def ok_response(self):
        return self.response(0, "Message put in the queue.")

def run(queue, port, server_class=socketserver.TCPServer, handler_class=MessageHandler):
    """ Create a server using parameters given and make it serve forever.

    Keyword Arguments:
        queue         - An instance of a queue to use to hold messages.
        port          - The port that the server has to listen.
        server_class  - The class to use for the server instanciation.
        handler_class - The handler that the server has to use.
    """
    global message_queue
    global instance
    message_queue = queue
    server_address = ('', port)
    instance = server_class(server_address, handler_class)
    instance.serve_forever()

def shutdown():
    """ Stop the server.
    """
    global instance
    if instance != None: # Shutdown only if the server has been created.
        instance.shutdown()
