# -*- coding: utf-8 -*-
""" Simple program to test the lcddaemon program.

    Purpose: Send random data (JSON format) through socket to the daemon.
"""

import json
import time
from http.client import HTTPConnection


class SimpleTester(object):
    """ Specify kind of messages to be send.
        This let the user choose which kind of messages,
        each kind has specific properties to test LCD Screen.
    """
    def __init__(self, generator):
        self.httpconnection = HTTPConnection("192.168.1.3", 8000)
        self.generator = generator
        self.counter = 0

    def send_next(self):
        """ Send message using the specified generator to the deamon.

            Return the time to wait until sending next message.
        """
        self.counter += 1
        msg_json, wait = self.generator(self.counter)

        msg_json = json.dumps(msg_json)

        self.httpconnection.request("POST", "/",
                                    headers={'Content-Length': len(msg_json)})
        self.httpconnection.send(bytes(msg_json, 'UTF-8'))

        httpresponse = self.httpconnection.getresponse()
        print(httpresponse.msg)
        print(httpresponse.read())
        self.httpconnection.close()

        return wait


def basic_messages(counter):
    """ Generate basic messages.

        Keyword arguments:
          content  - content to be displayed;
          sender   - program's name;
          duration - time for the message to be displayed.

        Return the message, the time the program must wait until sending next.
    """

    msg = {"content": "Simple Content n°" + str(counter),
           "sender": "SimpleTester",
           "duration": 20,
           "ttl": 60}

    return msg, 20


""" Main function to send messages of the choosen message type.
    The main function is processed undefinitely.
"""
if __name__ == '__main__':
    tester = SimpleTester(basic_messages)

    while True:
        wait = tester.send_next()
        time.sleep(wait)
