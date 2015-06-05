#-*- coding: utf-8 -*-
""" This script contains a simple driver that just print the string in cmd.
    This is use for test purpose.
"""

from drivers.abstractdriver import AbstractDriver

class CmdDriver(AbstractDriver):
    def line_count(self):
        return 1

    def line_size(self):
        return 99

    def write_lines(self, tuple_of_string):
        print(tuple_of_string[0])

    def clear(self):
        pass # We don't clear the screen
