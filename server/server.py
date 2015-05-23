#-*- coding: utf-8 -*-
""" This script defines the server object that is used to
    handle clients' messages.
"""

import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class MessageHandler(BaseHTTPRequestHandler):
    """ This object is the handler for messages.
        Messages are encoded as json.
    """
    def do_POST(self): #TODO
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)
        message_dict = json.loads(str(post_data, 'UTF-8'))
        print(message_dict)

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

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__': # For debug purpose 
    run(handler_class=MessageHandler)
