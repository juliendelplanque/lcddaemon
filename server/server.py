#-*- coding: utf-8 -*-
""" This script defines the server object that is used to
    handle clients' messages.
"""

import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from core.message import *

message_queue = None

class MessageHandler(BaseHTTPRequestHandler):
    """ This object is the handler for messages.
        Messages are encoded as json.
    """
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        message_dict = json.loads(str(post_data, 'UTF-8'))
        print("JSON received: "+str(message_dict))
        m = create_message_from_dict(message_dict)
        print("Message created: "+str(m))
        message_queue.put(m)
        print("Message is now in the queue.")
        print(str(message_queue))
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(bytes(self.ok_response(), 'UTF-8'))

    def response(self, code, message):
        return json.dumps({'code': code, 'message': message})

    def ok_response(self):
        return self.response(0, "Message put in the queue.")

    def error_response(self):
        return self.response(1, "Error, message not in the queue.")

def run(queue, port=4242, server_class=HTTPServer, handler_class=MessageHandler):
    global message_queue
    message_queue = queue
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
